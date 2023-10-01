from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from products.models import Lesson, LessonProgress
from products.serializers import LessonSerializer, LessonProgressSerializer

from products.models import Product
from products.serializers import ProductStatisticsSerializer


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Lesson.objects.filter(products__owner=user)

class LessonDetailAPIView(generics.RetrieveAPIView):
    serializer_class = LessonProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        return LessonProgress.objects.filter(user=user, lesson__product_id=product_id)

class ProductStatisticsAPIView(generics.ListAPIView):
    serializer_class = ProductStatisticsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        accessible_products = Product.objects.filter(owner=user)
        return accessible_products


