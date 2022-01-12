from rest_framework import serializers
from datetime import datetime

from calorie.food.models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'user', 'name', 'calorie', 'date')
        read_only_fields = ['id', 'user']
        extra_kwargs = {
            'date': {'required': True},
            'name': {'required': True},
            'calorie': {'required': True}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        date = validated_data.get('date', datetime.now())

        return Food.objects.create(
            user=user,
            name=validated_data['name'],
            calorie=validated_data['calorie'],
            date=date,
        )
