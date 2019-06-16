from rest_framework import generics
from .serializers import OrderDetailSerializer, OrderListSerializer
from .models import Order
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderDetailSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

class UserOrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    def get_queryset(self):
        owner_id = self.kwargs['owner_id']
        return Order.objects.filter(owner_id=owner_id)
