from django.urls import path

from .views import ListKjsieit, DetailKjsieit

urlpatterns = [
    path("", ListKjsieit.as_view()),
    path("<int:pk>/", DetailKjsieit.as_view())
]
