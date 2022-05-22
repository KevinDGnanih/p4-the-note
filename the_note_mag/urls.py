from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('edit_post/<slug:slug>', views.EditPost.as_view(), name='edit_post'),
    path('<slug:slug>/delete', views.DeletePost.as_view(), name='delete_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('category/<str:cats>', views.CategoryPosts.as_view(), name='category')
]
