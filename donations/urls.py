from django.urls import path
from .views import DonationListCreate, DonationRetrieve

urlpatterns = [
    path("", DonationListCreate.as_view()),
    path("<int:pk>", DonationRetrieve.as_view()),
]
