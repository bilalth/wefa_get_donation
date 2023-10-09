from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from donations.views import DonationModelViewSet

router = DefaultRouter()
router.register(r"", DonationModelViewSet, basename="donation")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api-token-auth/", views.obtain_auth_token),
    # path("donations/", include("donations.urls")),
    path("donations/", include(router.urls)),
]
