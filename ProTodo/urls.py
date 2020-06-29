"""ProTodo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Todos.views import todoView , addTodo , deleteTodo ,editTodo , editTodoConfirm ,todoSwitchState

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todoView ),
    path('addtodo/', addTodo ),
    path('deletetodo/<int:delete_item_id>', deleteTodo ),
    path('edittodo/<int:edit_item_id>', editTodo ),
    path('edittodoconfirm/<int:edit_item_id>', editTodoConfirm ),
    path('todoswitchstate/<int:edit_item_id>', todoSwitchState ),
]