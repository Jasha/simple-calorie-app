from rest_framework import serializers
from datetime import datetime

from calorie.food.models import Food


class FoodSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source="user.name")

    class Meta:
        model = Food
        fields = ('id', 'user', 'user_name', 'name', 'calorie', 'date')
        read_only_fields = ['id']
        extra_kwargs = {
            'user': {'required': True},
            'name': {'required': True},
            'calorie': {'required': True}
        }

    def create(self, validated_data):
        date = validated_data.get('date', datetime.now())

        return Food.objects.create(
            user=validated_data['user'],
            name=validated_data['name'],
            calorie=validated_data['calorie'],
            date=date,
        )


class ReportSerializer(serializers.Serializer):
    last_week_entries = serializers.IntegerField()
    previous_week_entries = serializers.IntegerField()


class UserReportSerializer(serializers.Serializer):
    name = serializers.CharField()
    average_calories = serializers.FloatField()
