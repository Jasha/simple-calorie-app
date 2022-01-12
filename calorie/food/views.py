from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from calorie.food.serializers import FoodSerializer
from calorie.food.models import Food


class FoodView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FoodSerializer
    pagination_class = None

    def get_queryset(self):
        return Food.objects.filter(
            user=self.request.user,
            date__gte=self.request.query_params.get('from_date'),
            date__lte=self.request.query_params.get('to_date'),
        ).order_by('-date')
