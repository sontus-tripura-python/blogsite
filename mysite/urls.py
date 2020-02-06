from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('post/',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
    path('post/new/', views.post_new, name='post_new'),
     path('draft/', views.post_draft, name='post_draft'),
     path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
     path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('contact',views.contact, name='contact'),
    path('contact',views.contact, name='contact'),
]
