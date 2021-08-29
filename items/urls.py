from django.urls import path
from . import views
 
app_name = "items"
 
urlpatterns = [
    path("", views.Index.as_view(), name="index"), # 一覧
    path("create/", views.Create.as_view(), name="create"), # 新規作成
    path("detail/<int:pk>/", views.Detail.as_view(), name="detail"), # 詳細
    path("order/<int:pk>", views.order, name="order"),
]