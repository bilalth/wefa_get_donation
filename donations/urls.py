from django.urls import path
from .views import DonationModelViewSet, DonationRetrieve

urlpatterns = [
    path("", DonationModelViewSet.as_view()),
    path("<int:pk>", DonationRetrieve.as_view()),
]
