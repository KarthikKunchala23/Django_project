from rest_framework import serializers
from .models import student

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model= student
        # fields=['id','name','mobile','address','email']
        fields='__all__' #consider million lines of data
        


