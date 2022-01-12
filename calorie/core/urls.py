from django.conf.urls import url

from calorie.core.views import LoginView, RegisterView, InviteView, ProfileView


urlpatterns = [
    url(r'login/', LoginView.as_view(), name='login'),
    url(r'register/', RegisterView.as_view(), name='register'),
    url(r'invite/', InviteView.as_view(), name='invite'),
    url(r'profile/', ProfileView.as_view(), name='profile'),
]
