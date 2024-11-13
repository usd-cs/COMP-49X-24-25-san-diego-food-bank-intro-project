"""This module contains the configuration for the WebForum app."""

from django.apps import AppConfig

class WebForumConfig(AppConfig):
    """Configuration for the WebForum app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web_forum'

    def ready(self):
        """
        Perform any application-specific startup tasks.
        """
        pass
