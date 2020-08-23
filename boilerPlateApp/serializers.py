from rest_framework import serializers
from boilerPlateApp.models import basic

class basicSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model=basic
        # fields=('card_number','exp_date', 'cvv')
        fields='__all__'