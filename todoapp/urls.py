from django.urls import path
from .import views as v

app_name = "todo"

urlpatterns = [
    path('', v.index, name="index"),
    path('addtodo', v.add_todo, name="add_todo"),
    path('detailtodo/<int:pk>', v.detail_todo, name="detail_todo"),
]
