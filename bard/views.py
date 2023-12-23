from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .forms import *
from .utils import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import TestResult, Test


from .models import MathTopic

from django.shortcuts import render


def math_topic_details(request, topic_id):
    topic = MathTopic.objects.get(pk=topic_id)
    test_id = ...
    context = {
        'topic': topic,
        'your_test_id': test_id  # убедитесь, что здесь правильный test_id
    }
    return render(request, 'topic_details.html', {'topic': topic})


def test_view(request, test_id):
    # Убедитесь, что вы используете test_id как целое число для получения теста
    test = Test.objects.get(id=test_id)
    questions = Question.objects.filter(test=test)

    # остальная часть вашего кода
    return render(request, 'test.html', {'test': test, 'questions': questions})


@login_required
def profile(request):
    user = request.user
    tests = Test.objects.all()  # Получите все тесты, которые вам нужны для профиля пользователя

    # Создайте словарь, где ключами будут тесты, а значениями будут результаты пользователя
    test_results = {}
    for test in tests:
        user_test_result = TestResult.objects.filter(user=user, test=test).first()
        test_results[test] = user_test_result

    context = {
        'user': user,
        'tests': tests,
        'test_results': test_results,
    }

    return render(request, 'profile.html', context)


class Home(DataMixin, ListView):
    model = Women
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация / Тіркелу")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация / Авторландыру")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def process_test(request, test_id):
    if request.method == 'POST':
        try:
            test = Test.objects.get(id=test_id)
            user = request.user
            score = 0

            for question in test.question_set.all():
                user_answer = request.POST.get(str(question.id))
                correct_answer = question.answer_set.filter(is_correct=True).first()
                if user_answer == correct_answer.text:
                    score += 1

            # Найти или создать запись в TestResult для данного пользователя и теста
            user_test_result, created = TestResult.objects.get_or_create(user=user, test=test)

            # Обновляем последний результат
            user_test_result.score = score

            # Обновляем лучший результат, если он лучше предыдущего
            if score > user_test_result.best_score:
                user_test_result.best_score = score

            user_test_result.save()

            return redirect('profile')

        except Test.DoesNotExist:
            return redirect('profile')

class Home2(DataMixin, ListView):
    model = Women
    template_name = 'base2.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Басты бет")
        return dict(list(context.items()) + list(c_def.items()))
    def get_success_url(self):
        return redirect('home2')