from datetime import datetime as dt
import datetime

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django.db.models import Sum

from calorie.food.admin.serializers import FoodSerializer, ReportSerializer, UserReportSerializer
from calorie.food.models import Food, User


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class AdminFoodView(generics.ListCreateAPIView):
    queryset = Food.objects.all().order_by("-date")
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = FoodSerializer
    pagination_class = PageNumberPagination


class AdminFoodDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = FoodSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.user_id = request.data.get("user_id")
        instance.name = request.data.get("name")
        instance.calorie = request.data.get("calorie")
        instance.date = request.data.get("date", dt.now())
        instance.save()

        serializer = self.get_serializer(instance)

        return Response(serializer.data)


class AdminFoodReportView(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = ReportSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        now = dt.now()
        last_week = now - datetime.timedelta(days=7)
        previous_week = last_week - datetime.timedelta(days=7)

        last_week_entries = Food.objects.order_by("date").filter(date__lte=now, date__gt=last_week).count()
        previous_week_entries = Food.objects.order_by("date").filter(date__lte=last_week, date__gt=previous_week).count()

        return Response({
            "last_week_entries": last_week_entries,
            "previous_week_entries": previous_week_entries,
        })


class AdminFoodUserReportView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = UserReportSerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        now = dt.now()
        last_week = now - datetime.timedelta(days=7)

        user_calories = User.objects.select_related("food").filter(food__date__lte=now, food__date__gt=last_week).annotate(average_calories=Sum("food__calorie") / 7).values("name", "average_calories")

        return Response(user_calories)
