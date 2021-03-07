from rest_framework import serializers
from api.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('username','password','address')
