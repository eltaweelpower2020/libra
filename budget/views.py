
from django.shortcuts import render

from budget.models import LibraBudget
from .forms import LibraBudgetform
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
     budget_all=LibraBudget.objects.all()


     return render(request,'home.html',{'budget_all':budget_all})

@login_required(login_url='/login/')
def add_budget_lead(request):
     form = LibraBudgetform()
     if request.method =='POST':
        form = LibraBudgetform(request.POST)
        if form.is_valid():
               libra_budget = form.save(commit=False)
               libra_budget.added_by=request.user
               libra_budget.save()
               return redirect('home')

     return render(request,'add_budget.html',{'form':form})

