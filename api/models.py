from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    def create(self,validated_data):
        """
        Create and return a new `Customer` instance, given the validated data.
        """
        return Customer.objects.create(**validated_data)
    def update(self, validated_data):
        """
        Update and return an existing `Customer` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
    # class Meta:
    #     ordering = ['username']

