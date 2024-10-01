from django.urls import path
from . import views

from rest_framework.routers import SimpleRouter
from .views import create_poster

router = SimpleRouter()
router.register(r'Poster', create_poster, basename='poster')


urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('<int:post_id>/', views.post.as_view(), name='post'),
    path('create_poster', views.create_poster.as_view(), name='create_poster')
]