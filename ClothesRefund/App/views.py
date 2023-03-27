from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Clothes
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from .forms import ClothesForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
#This is the index page, it contains the introduction of the website.
@login_required
def index(request):
    userid=request.user.id
    return render(request,"App/index.html",{'introduction':"bienvenue a tous", 'userid':userid})

#This is the page to add clothes, it contains the name, the material, the size, the brand and the color of the clothes that the user wants to add.

@login_required
def addclothes(request):
    userid=request.user.id
    if request.method == 'POST':
        name = request.POST.get('name')
        material = request.POST.get('material')
        size = request.POST.get('size')
        brand = request.POST.get('brand')
        color = request.POST.get('color')
        clothes = Clothes(ClothesName=name,ClothesMaterial=material,ClothesSize=size,ClothesBrand=brand,ClothesColor=color)
        clothes.save()
        return HttpResponseRedirect("../"+"/addclothes")
    return render(request,"App/addclothes.html",{'userid':userid})

#This is the page to remove clothes, the filter get the clothes that the user wants to remove, and the delete function delete the clothes. I used the name of the clothes to filter it. I check if the name of the clothes is in the database, if it is, I delete it. I do that to avoid the error if the user wants to delete a clothes that is not in the database, and to not redirect the user to an error page.

@login_required
def remove_clothes(request):
    userid=request.user.id
    form = ClothesForm()
    if request.method == 'POST':
        form = ClothesForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            clothes = Clothes.objects.filter(ClothesName=clean['ClothesName'])
            if len(clothes)==1:
                clothes[0].delete()
                return HttpResponseRedirect("../"+"/remove_clothes")
    return render(request,"App/remove_clothes.html",{'form':form, 'userid':userid})


# This is the page to edit clothes, the filter get the clothes that the user wants to edit, and the save function save the clothes. I used the name of the clothes to filter it. I check if the name of the clothes is in the database, if it is, I edit it. I do that to avoid the error if the user wants to edit a clothes that is not in the database, and to not redirect the user to an error page. This works as same as the page to create clothes.

@login_required
def edit_clothes(request):
    userid=request.user.id
    form = ClothesForm()
    if request.method == 'POST':
        form = ClothesForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            clothes = Clothes.objects.filter(ClothesName=clean['ClothesName'])
            if len(clothes)==1:
                clothes[0].ClothesName = request.POST.get('name')
                clothes[0].ClothesMaterial = request.POST.get('material')
                clothes[0].ClothesSize = request.POST.get('size')
                clothes[0].ClothesBrand = request.POST.get('brand')
                clothes[0].ClothesColor = request.POST.get('color')
                clothes[0].save()
                return HttpResponseRedirect("../"+"/edit_clothes")
    return render(request,"App/edit_clothes.html",{'form':form, 'userid':userid})

@login_required
def clothes_list(request):
    userid=request.user.id
    clothes_list = Clothes.objects.all()
    return render(request,"App/clothes_list.html",{'clothes_list':clothes_list, 'userid':userid})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


