from django.contrib import admin

from server.apps.main.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin[BlogPost]):
    """Admin panel example for ``BlogPost`` model."""


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin[User]):
#     """Admin panel example for ``User`` model."""
