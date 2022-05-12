
from django.urls import path
from .views import deleteTodo, detailTodo, home, liste,createTodo, updateTodo

urlpatterns = [
    path('', home, name='home'),
    path('liste/', liste, name='liste'),
    path('create/', createTodo, name='create'),
    path('update/<int:id>', updateTodo, name='update'),
    path('detail/<int:id>', detailTodo, name='detail'),
    path('delete/<int:id>', deleteTodo, name='delete'),

]