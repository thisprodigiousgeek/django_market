from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin # 追記
from django.contrib.auth import get_user_model

from .forms import SignupForm, LoginForm



class SignUp(generic.CreateView):
    form_class = SignupForm # 利用するフォームクラスを設定
    template_name = "accounts/sign_up.html"
 
    def get_success_url(self):
        return reverse_lazy("items:index") 
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ユーザー登録"
        return context
    
# ログイン
class Login(LoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ログイン"
        return context
    
# ログアウト
class Logout(LogoutView):
    template_name = "accounts/logout.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ログアウトしました"
        return context