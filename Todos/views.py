from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from .models import TodoItem


# Create your views here.
def todoView(request):
    # get the list, and sort the list by latest datestamp
    allItems = TodoItem.objects.all().order_by('-timestamp')
    return render(request,"todo.html", {'all_Items': allItems} )

def addTodo(request):
    # add a new item
    # save
    # redirect to previous page
    new_item = TodoItem(content = request.POST['content'],timestamp=timezone.now(),target_timestamp=request.POST['target_datetime'])
    new_item.save()
    messages.success(request,"Your Todo was saved successfully")
    return HttpResponseRedirect('/todo/')

def deleteTodo(request , delete_item_id ):
    delete_item = TodoItem.objects.get(id=delete_item_id)
    delete_item.delete()
    messages.error(request, "Item has been hard deleted")
    return HttpResponseRedirect('/todo/')

def editTodo(request , edit_item_id ):
    edit_item = TodoItem.objects.get(id=edit_item_id)
    return render(request, "edittodo.html", {'edit_item': edit_item})

def editTodoConfirm(request , edit_item_id):
    _edit_item = TodoItem.objects.get(id=edit_item_id)
    _edit_item.content = request.POST['content']
    _edit_item.target_timestamp = request.POST['target_datetime']
    _edit_item.save()

    messages.success(request, "Todo was updated successfully!" )
    return HttpResponseRedirect('/todo/')