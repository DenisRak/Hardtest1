from django.urls import path


from api.views import LessonListAPIView, LessonDetailAPIView, ProductStatisticsAPIView



urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
    path('product-statistics/', ProductStatisticsAPIView.as_view(), name='product-statistics'),

]
