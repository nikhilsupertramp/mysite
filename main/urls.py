"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import views

app_name="main" 

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("register/",views.register,name="register"),
    path('submit/',views.submit,name='submit'),
    path('scholar/',views.scholar,name='scholar'),
    path('sdg/',views.sdg,name='sdg'),
    path('sdg/no_poverity/',views.no_poverity,name='no_poverity'),
	path('sdg/no_poverity/submit',views.submit,name='submit'),
	path('sdg/zero_hunger/',views.zero_hunger,name='zero_hunger'),
	path('sdg/zero_hunger/submit',views.submit,name='submit'),
	path('sdg/health/',views.health,name='health'),
	path('sdg/health/submit',views.submit,name='submit'),
	path('sdg/quality_education/',views.quality_education,name='quality_education'),
	path('sdg/quality_education/submit',views.submit,name='submit'),
	path('sdg/gender_equality/',views.gender_equality,name='gender_equality'),
	path('sdg/gender_equality/submit',views.submit,name='submit'),
	path('sdg/water_goals/',views.water_goals,name='water_goals'),
	path('sdg/water_goals/submit',views.submit,name='submit'),
	
	path('sdg/clean_energy/',views.clean_energy,name='clean_energy'),
	path('sdg/clean_energy/submit',views.submit,name='submit'),
	
	path('sdg/decent_work/',views.decent_work,name='decent_work'),
	path('sdg/decent_work/submit',views.submit,name='submit'),
	
	path('sdg/industry_innovation/',views.industry_innovation,name='industry_innovation'),
	path('sdg/industry_innovation/submit',views.submit,name='submit'),
	
	path('sdg/reduced_inequalities/',views.reduced_inequalities,name='reduced_inequalities'),
	path('sdg/reduced_inequalities/submit',views.submit,name='submit'),
	
	path('sdg/sustainaible_cities/',views.sustainaible_cities,name='sustainaible_cities'),
	path('sdg/sustainaible_cities/submit',views.submit,name='submit'),
	
	path('sdg/responsible_consumption/',views.responsible_consumption,name='responsible_consumption'),
	path('sdg/responsible_consumption/submit',views.submit,name='submit'),
	
	path('sdg/climate_action/',views.climate_action,name='climate_action'),
	path('sdg/climate_action/submit',views.submit,name='submit'),
	
	path('sdg/water_life/',views.water_life,name='water_life'),
	path('sdg/water_life/submit',views.submit,name='submit'),
	
	path('sdg/life_on_land/',views.life_on_land,name='life_on_land'),
	path('sdg/life_on_land/submit',views.submit,name='submit'),
	
	path('sdg/peace_justice/',views.peace_justice,name='peace_justice'),
	path('sdg/peace_justice/submit',views.submit,name='submit'),
	
	path('sdg/partnerships_for_goals/',views.partnerships_for_goals,name='partnerships_for_goals'),
	path('sdg/partnerships_for_goals/submit',views.submit,name='submit'),
]
