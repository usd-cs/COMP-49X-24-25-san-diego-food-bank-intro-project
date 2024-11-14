# Generated by Django 5.1.3 on 2024-11-14 00:25

from django.db import migrations
from web_forum.models import User

def create_base_users(apps, schema_editor):
    User.objects.create_user(
        username= 'Billy Bob',
        email= 'billybob@sandiego.edu',
        password= 'BillyTheBob'
    )

    User.objects.create_user(
        username= 'foodbank',
        email= 'foodbank@sandiego.edu',
        password= 'fb_123',
        admin = True,
    )

class Migration(migrations.Migration):
    
    dependencies = [
        ('web_forum', '0002_rename_content_comment_contents_and_more'),
    ]

    operations = [
        migrations.RunPython(create_base_users)
    ]
