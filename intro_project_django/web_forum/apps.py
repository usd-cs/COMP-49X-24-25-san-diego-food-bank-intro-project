"""Temp docstring for linting"""
from django.apps import AppConfig

class WebForumConfig(AppConfig):
    """Temp docstring for linting"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web_forum'
    def ready(self):
        """
        Temp to override linting
        """
        pass
