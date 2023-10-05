from rest_framework import serializers
from .models import Donation


class DonationSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_name = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Donation
        fields = ["id", "user_name", "amount", "date", "description", "campaign"]
        # fields = ["id", "user", "amount", "date", "description", "campaign"]
