from django.urls import path,include
from .views import DonationModelViewSet
from donations.views import DonationModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"", DonationModelViewSet, basename="donation")
urlpatterns = [
    path("", include(router.urls)),
    # path("", DonationModelViewSet.as_view()),
    # path("<int:pk>", DonationRetrieve.as_view()),
]
