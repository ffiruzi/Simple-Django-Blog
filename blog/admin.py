

from django.contrib import admin
from .models import Post, Category, UserProfile
from .models import Comment
from .models import Tag

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'website')
    search_fields = ('user__username', 'user__email')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'category', 'author', 'view_count', 'is_featured')
    list_filter = ('pub_date', 'category', 'author', 'is_featured')
    actions = ['make_featured', 'remove_featured']
    search_fields = ('title', 'content')
    readonly_fields = ('view_count',)

    def make_featured(self, request, queryset):
        queryset.update(is_featured=True)

    make_featured.short_description = "Mark selected posts as featured"

    def remove_featured(self, request, queryset):
        queryset.update(is_featured=False)

    remove_featured.short_description = "Remove selected posts from featured"


# Add this to register the Comment model with the admin site
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_date', 'is_approved')
    list_filter = ('created_date', 'is_approved', 'author')
    search_fields = ('content', 'author__username', 'post__title')
    actions = ['approve_comments', 'disapprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)

    approve_comments.short_description = "Approve selected comments"

    def disapprove_comments(self, request, queryset):
        queryset.update(is_approved=False)

    disapprove_comments.short_description = "Disapprove selected comments"


admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Tag)