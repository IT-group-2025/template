from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.TestPageView.as_view(), name='test_page'),
    path('style_test/', views.StyleTestPageView.as_view(), name='style_test_page'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
]