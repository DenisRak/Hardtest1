from rest_framework import serializers
from .models import Lesson, LessonProgress
from .models import Product


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonProgress
        fields = '__all__'

class ProductStatisticsSerializer(serializers.ModelSerializer):
    total_viewed_lessons = serializers.SerializerMethodField()
    total_viewing_time = serializers.SerializerMethodField()
    total_users = serializers.SerializerMethodField()
    product_purchase_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'total_viewed_lessons', 'total_viewing_time', 'total_users', 'product_purchase_percentage']

    def get_total_viewed_lessons(self, obj):

        return obj.lessons.filter(lessonprogress__status='Viewed').count()

    def get_total_viewing_time(self, obj):
        # Расчет общего времени просмотра уроков для продукта
        return obj.lessons.filter(lessonprogress__status='Viewed').aggregate(
            total_time=models.Sum('lessonprogress__viewed_time_seconds'))['total_time']

    def get_total_users(self, obj):
        # Расчет общего числа пользователей, имеющих доступ к продукту
        return obj.owner.all().count()

    def get_product_purchase_percentage(self, obj):

        total_users = self.get_total_users(obj)
        if total_users > 0:
            access_count = obj.owner.count()
            return (access_count / total_users) * 100
        return 0



