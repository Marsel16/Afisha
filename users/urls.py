from django.urls import path
from users.views import AuthorizationCreateAPIView, RegisterCreateAPIView
urlpatterns = [
    path('authorization/', AuthorizationCreateAPIView.as_view()),
    path('register/', RegisterCreateAPIView.as_view())
]
