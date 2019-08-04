from django.shortcuts import render,redirect
from .scholarscrape import scholarscrapy
from django.http import HttpResponse
from .models import Interns
from .models import keyword
from .models import sdg1,sdg2,sdg3,sdg4,sdg5,sdg6,sdg7,sdg8,sdg9,sdg10,sdg11,sdg12,sdg13,sdg14,sdg15,sdg16,sdg17
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate   
from .gwst2 import fun


# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name="main/home.html")
 
def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
           user=form.save()
           login(request,user)
           return redirect("main:homepage")
        else:
           for msg in form.error_messages:
              print(form.error_messages[msg])


   
    form = UserCreationForm
    return render(request,
                  "main/register.html",
                   context={"form":form})


def scholar(request):
     if request.method=="GET":
        query=request.GET.get('keyW')
        message="hello the keyword is {}".format(query)
        html=scholarscrapy(query)
        return HttpResponse(html)
    
    
def submit(request):
    if request.method=="GET":
        query=request.GET.get('keyW')
        message="hello the keyword is {}".format(query)
        html=fun(query)
        return  HttpResponse(html)


def sdg(request):
    return render(request = request,
                  template_name="main/sdg.html")

def no_poverity(request):
    return render(request = request,
                  template_name="main/no_poverity.html",
                 context={"sdg1":sdg1.objects.all})

def zero_hunger(request):
    return render(request = request,
                  template_name="main/zero_hunger.html",
                 context={"sdg2":sdg2.objects.all})

def health(request):
    return render(request = request,
                  template_name="main/health.html",
                 context={"sdg3":sdg3.objects.all})

def quality_education(request):
    return render(request = request,
                  template_name="main/quality_education.html",
                 context={"sdg4":sdg4.objects.all})

def gender_equality(request):
    return render(request = request,
                  template_name="main/gender_equality.html",
                 context={"sdg5":sdg5.objects.all})

def water_goals(request):
    return render(request = request,
                  template_name="main/water_goals.html",
                 context={"sdg6":sdg6.objects.all})

def clean_energy(request):
    return render(request = request,
                  template_name="main/clean_energy.html",
                 context={"sdg7":sdg7.objects.all})

def decent_work(request):
    return render(request = request,
                  template_name="main/decent_work.html",
                 context={"sdg8":sdg8.objects.all})

def industry_innovation(request):
    return render(request = request,
                  template_name="main/industry_innovation.html",
                 context={"sdg9":sdg9.objects.all})

def reduced_inequalities(request):
    return render(request = request,
                  template_name="main/reduced_inequalities.html",
                 context={"sdg10":sdg10.objects.all})

def sustainaible_cities(request):
    return render(request = request,
                  template_name="main/sustainaible_cities.html",
                 context={"sdg11":sdg11.objects.all})

def responsible_consumption(request):
    return render(request = request,
                  template_name="main/responsible_consumption.html",
                 context={"sdg12":sdg12.objects.all})

def climate_action(request):
    return render(request = request,
                  template_name="main/climate_action.html",
                 context={"sdg13":sdg13.objects.all})

def water_life(request):
    return render(request = request,
                  template_name="main/water_life.html",
                 context={"sdg14":sdg14.objects.all})

def life_on_land(request):
    return render(request = request,
                  template_name="main/life_on_land.html",
                 context={"sdg15":sdg15.objects.all})


def peace_justice(request):
    return render(request = request,
                  template_name="main/peace_justice.html",
                 context={"sdg16":sdg16.objects.all})

def partnerships_for_goals(request):
    return render(request = request,
                  template_name="main/partnerships_for_goals.html",
                 context={"sdg17":sdg17.objects.all})