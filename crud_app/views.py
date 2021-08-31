from django.shortcuts import render,redirect
from . models import CRUD
from . forms import CreateModelform

# Create your views here.

def home(request):
    return render(request, "crud_app/home.html")

def create(request):
    form = CreateModelform()
    if request.method == "POST":
        form = CreateModelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "crud_app/create.html", context)

def retrive_list(request):
    list_of_text = CRUD.objects.all().order_by("-date_added")

    context = {
        "list_of_text": list_of_text
    }
    return render(request, "crud_app/retrive_list.html", context)

def update_text(request):
    update_list = CRUD.objects.all().order_by("-date_added")

    context = {
        "update_list": update_list
    }
    return render(request, "crud_app/update_list.html", context)

def update(request, pk):
    text = CRUD.objects.get(id=pk)
    form = CreateModelform(instance=text)
    if request.method == "POST":
        form = CreateModelform(request.POST, instance=text)
        if form.is_valid():
            form.save()
            return redirect("/list/")
    
    context = {
        "text": text,
        "form": form 
    }
    return render(request, "crud_app/update.html", context)

def delete_text(request):
    delete_list = CRUD.objects.all().order_by("-date_added")

    context = {
        "delete_list": delete_list
    }
    return render(request, "crud_app/delete.html", context)

def delete(request, pk):
    text = CRUD.objects.get(id=pk)
    text.delete()
    return redirect("/delete/")