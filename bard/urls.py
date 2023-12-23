from django.urls import path, re_path


from . import views
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('topics/<int:topic_id>/', math_topic_details, name='topic_details'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('test/<int:test_id>/', views.test_view, name='test_view'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('kz/', Home2.as_view(), name="home2")
]
