from django.urls import path, include
from .views import *

urlpatterns = [
    path('order/create/', OrderCreateView.as_view()),
    path('all/', OrderListView.as_view()),
    path('order/detail/<int:pk>', OrderDetailView.as_view()),
    path('user/<owner_id>/orders/', UserOrderListView.as_view()),# TODO: I have to define owner type
]
