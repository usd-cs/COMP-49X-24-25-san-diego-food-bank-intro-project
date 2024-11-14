from django.test import TestCase
from .models import User, Post, Comment
from django.urls import reverse
"""Temp docstring for linting"""

class UserModelTest(TestCase):
    def test_user_creation(self):
        # Create user
        user = User.objects.create_user(username='testuser', password='testpass')

        # Check user fields 
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpass')) # Deal with DJango password hashing with check_password
        self.assertFalse(user.admin)

class PostModelTest(TestCase):
    def setUp(self):
        # Create user for post 
        self.user = User.objects.create_user(username='test', password='passw')
    
    def test_post_creation(self):
        #Create post by the user
        post = Post.objects.create(user=self.user, contents="this is a test post")

        self.assertEqual(post.user, self.user)
        self.assertEqual(post.contents, "this is a test post")
        self.assertIsNotNone(post.created_at)

class CommentModelTest(TestCase):
    def setUp(self):
        # Create user and post for the comment 
        self.user = User.objects.create_user(username='testuser', password='passw')
        self.post = Post.objects.create(user=self.user, contents='test post')
    
    def test_comment_creation(self):
        # Create comment on the post by the user
        comment = Comment.objects.create(post=self.post, user=self.user, contents='test post')
        # Check that the comment is created and is associated with correct user and post
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.contents, 'test post')
        self.assertIsNotNone(comment.created_at)

class LoginViewTest(TestCase):
    def setUp(self):
        # Create user for login 
        self.username = 'test user'
        self.password = 'password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
    
    def test_successful_login(self):
        # Test the login with correct login credentials
        response = self.client.post(reverse('login'), {
            'username': self.username,
            'password': self.password,
        })

        self.assertRedirects(response, reverse('home'))
    
    def test_unsuccessful_login(self):
        # Test login with a username that doesn't exist 
        response = self.client.post(reverse('login'), {
            'username': 'nonexistantuser',
            'password': 'password123',
        })

        # Log in page should have an error 
        self.assertEqual(response.status_code, 200)

class HomeViewTest(TestCase):
    def setUp(self):
        # Create regular user and an admin user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.admin_user = User.objects.create_user(username='adminuser', password='adminpass', admin=True)

        # Create post as regular user 
        self.post = Post.objects.create(user=self.user, contents='This is a test post')