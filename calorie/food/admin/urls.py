from django.conf.urls import url

from calorie.food.admin.views import AdminFoodView, AdminFoodDetailsView, AdminFoodReportView, AdminFoodUserReportView


urlpatterns = [
    url(r'^$', AdminFoodView.as_view(), name='admin-food'),
    url(r'^(?P<pk>\d+)/$', AdminFoodDetailsView.as_view(), name='admin-food-details'),
    url(r'^report-one/$', AdminFoodReportView.as_view(), name='admin-food-report'),
    url(r'^report-two/$', AdminFoodUserReportView.as_view(), name='admin-food-user-report'),
]
