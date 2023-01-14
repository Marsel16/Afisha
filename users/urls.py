from django.urls import path
from users.views import authorization_view, register_view
urlpatterns = [
    path('authorization/', authorization_view),
    path('register/', register_view)
]
