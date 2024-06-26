from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('posts/', views.posts, name='posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('submit-review/', views.submit_review, name='submit_review'),
    path('hobbies/standart/', views.standart, name='standart'),
    path('hobbies/calisthenics/', views.calisthenics, name='calisthenics'),
    path('hobbies/swimming/', views.swimming, name='swimming'),
    path('hobbies/basketball/', views.basketball, name='basketball')
]