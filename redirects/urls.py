from django.urls import path

from .views import FlyersView

urlpatterns = [
    path("flyers", FlyersView.as_view(), name="flyers")
]
