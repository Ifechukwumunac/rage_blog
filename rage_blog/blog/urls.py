from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.PostListView.as_view(), name="all"),
    path("read/<int:pk>/<slug:post>", views.post_detail, name="post_detail"),
    path('comment/reply/', views.reply_page, name="reply"),
]