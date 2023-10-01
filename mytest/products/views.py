

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Lesson, LessonProgress, LessonAccess
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'base.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    lessons = product.lessons.all()
    context = {'product': product, 'lessons': lessons}
    return render(request, 'product_detail.html', context)

@login_required
def user_profile(request, user_id):
    user = request.user
    products = Product.objects.filter(owner=user)
    lessons = Lesson.objects.filter(products__owner=user)

    context = {'user': user, 'products': products, 'lessons': lessons}
    return render(request, 'user_profile.html', context)


@login_required
def view_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    user = request.user
    lesson_progress, created = LessonProgress.objects.get_or_create(user=user, lesson=lesson)

    if request.method == "POST":
        viewed_time_seconds = int(request.POST.get("viewed_time_seconds"))
        lesson_progress.viewed_time_seconds = viewed_time_seconds
        lesson_progress.mark_as_viewed()
        lesson_progress.updated_at = timezone.now()
        lesson_progress.save()

    return render(request, 'view_lesson.html', {'lesson': lesson, 'lesson_progress': lesson_progress})

@login_required
def add_lesson_to_profile(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    user = request.user
    LessonAccess.objects.get_or_create(user=user, lesson=lesson)
    return redirect('profile')

@login_required
def profile(request):
    user = request.user
    lesson_access_list = LessonAccess.objects.filter(user=user)
    return render(request, 'profile.html', {'lesson_access_list': lesson_access_list})

