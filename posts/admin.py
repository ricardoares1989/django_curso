# Django
from django.contrib import admin


from posts.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user','profile',
        'title', 'photo')
    list_display_links = ('pk', 'title','photo')
    search_fields= (
            'title', 'user__first_name', 
            'profile__phone_number')
    list_filter =(
        'created',
        'modified',
       )
    fieldsets = (
        ('Profile', {
            "fields": (
                'user',
                'profile',
            ),
        }),
        ('Post',{
            'fields': (
                'title',
                'photo',
            )
        }),
    )
    