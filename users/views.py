from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.views.generic import FormView

from .models import User
from .forms import RegisterForm, LoginForm, WithdrawalForm


class WithdrawalView(FormView):
    template_name = 'auth/withdrawal.html'
    form_class = WithdrawalForm
    success_url = '/auth/login'

    def form_valid(self, form):
        try:
            user = User.objects.get(email=self.request.user.email)
            if not user.check_password(form.cleaned_data.get('password')):
                raise User.DoesNotExist
        except User.DoesNotExist:
            messages.error(self.request, '비밀번호가 잘못되었습니다.', extra_tags='danger')
            return super().form_invalid(form)

        user.delete()
        messages.error(self.request, '탈퇴에 성공하였습니다.', extra_tags='info')
        return super().form_valid(form)


class RegisterView(FormView):
    template_name = 'auth/register.html'
    form_class = RegisterForm
    success_url = '/auth/login/'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = User(
            email=email,
            username=username,
        )
        user.set_password(password)
        user.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'auth/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
            if not user.check_password(form.cleaned_data.get('password')):
                raise User.DoesNotExist
        except User.DoesNotExist:
            messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
            return super().form_invalid(form)

        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect('/auth/login/')
