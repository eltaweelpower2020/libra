from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('add-budget',views.add_budget_lead,name='add_budget_lead'),

]
