from django.contrib import admin
from .models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','pk', 'status','created',)
    list_filter = ("status",'created')
    search_fields = ['title', 'body']

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display=('post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ( 'body',)
    
admin.site.register(Comment, CommentAdmin)