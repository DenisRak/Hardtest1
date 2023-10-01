

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField(blank=True)
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

class LessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_time_seconds = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=[("Not Viewed", "Не просмотрено"), ("Viewed", "Просмотрено")])


    def mark_as_viewed(self):
        if (self.viewed_time_seconds / self.lesson.duration_seconds) >= 0.8:
            self.status = "Просмотрено"
        else:
            self.status = "Не просмотрено"

class LessonAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.name}"


