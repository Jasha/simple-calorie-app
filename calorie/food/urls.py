from django.conf.urls import url

from calorie.food.views import FoodView


urlpatterns = [
    url(r'', FoodView.as_view(), name='food'),
]
