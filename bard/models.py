import random
from django.utils import timezone
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import uuid

from django.db import models
from django.contrib.auth.models import User


class Classroom(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Globally unique name
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='classrooms', blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    classrooms = models.ManyToManyField(Classroom, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Test(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title  # Возвращает название теста


class ClassroomJoinRequest(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)  # Принят или нет запрос
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Запрос от {self.student.username} в класс {self.classroom.name}"

class UserTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()
    percentage = models.DecimalField(max_digits=5, decimal_places=2)  # Поле для хранения процентов

    def calculate_percentage(self):
        total_questions = self.test.question_set.count()
        if total_questions > 0:
            correct_answers = self.score
            percentage = (correct_answers / total_questions) * 100
            return round(percentage, 2)
        else:
            return 0.00

    def save(self, *args, **kwargs):
        self.percentage = self.calculate_percentage()
        super().save(*args, **kwargs)

def get_default_date_taken():
    return timezone.now()
class TestResult(models.Model):
    date_taken = models.DateTimeField(default=get_default_date_taken)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    best_score = models.IntegerField(default=0)

    def __str__(self):
        return f"Результат теста {self.test.title} для пользователя {self.user.username}: Последний балл - {self.score}, Лучший балл - {self.best_score}"






class MathTopic(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = RichTextField()
    math_topic = models.ForeignKey(MathTopic, on_delete=models.SET_NULL, null=True, blank=True)
    # Остальные поля...
    def save(self, *args, **kwargs):
        # Удаляем HTML-теги из текста перед сохранением
        self.text = strip_tags(self.text)
        super(Question, self).save(*args, **kwargs)

class Language(models.Model):
    code = models.CharField(max_length=10, unique=True)  # Например, 'ru' или 'kz'

    def __str__(self):
        return self.code

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = RichTextField()
    is_correct = models.BooleanField(default=False)
    # Остальные поля...


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


from django.db import models
from django.contrib.auth.models import User

class TestResult1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.test_name} - {self.score}"
