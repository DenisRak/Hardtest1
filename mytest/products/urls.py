import profile

from django.urls import path
from products.views import product_list, product_detail, user_profile, view_lesson

from products.views import add_lesson_to_profile, profile

urlpatterns = [

    path('', product_list, name='index'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('profile/<int:user_id>/', user_profile, name='user_profile'),
    path('view-lesson/<int:lesson_id>/', view_lesson, name='view_lesson'),
    path('add-lesson-to-profile/<int:lesson_id>/', add_lesson_to_profile, name='add_lesson_to_profile'),
    path('profile/', profile, name='profile'),
]