from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .models import Item
from .forms import ItemCreateForm

class Index(LoginRequiredMixin, generic.ListView):
    template_name = "items/index.html"
    model = Item
    ordering = "-created_at"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品一覧"
        return context

class Create(LoginRequiredMixin, generic.CreateView):
    model = Item
    form_class = ItemCreateForm
    template_name = "items/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "新規出品"
        return context

    def form_valid(self, form):
        item = form.save(commit=False)
        item.user = self.request.user
        item.save()
        return redirect("items:index")
 
class Detail(LoginRequiredMixin, generic.DetailView):
    model = Item
    template_name = "items/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "商品詳細"
        return context

def order(request,pk):
    item = get_object_or_404(Item, pk=pk)
    item.orders.add(request.user)
    return redirect("items:index")