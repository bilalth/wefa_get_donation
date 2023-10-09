from rest_framework import generics, viewsets
from .models import Donation
from .serializers import DonationSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

class DonationModelViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    http_method_names = ["get"]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Donation.objects.all()
        return Donation.objects.filter(user=self.request.user)

# class DonationListCreate(generics.ListCreateAPIView):
#     serializer_class = DonationSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             return Donation.objects.all()
#         return Donation.objects.filter(user=self.request.user)
    



class DonationRetrieve(generics.RetrieveAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated, IsOwner]
