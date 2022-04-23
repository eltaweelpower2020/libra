
from django.shortcuts import render

from budget.models import LibraBudget
from .forms import LibraBudgetform
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
     budget_all=LibraBudget.objects.all()
     budget_asset_total=0
     budget_salary_total=0
     for budget in budget_all:
          check=budget.amount
          if check >0:
               budget_asset_total += budget.amount
          else:
               budget_salary_total += budget.amount
     print(budget_asset_total,'budget_asset_total')
     print(budget_salary_total,'budget_salary_total')
     budget_avaliable_total=budget_asset_total+budget_salary_total
     profit=False
     if budget_avaliable_total >0:
          profit=True

          


     return render(request,'home.html',
                    {'budget_all':budget_all,
                    'budget_asset_total':budget_asset_total,
                    'budget_salary_total':budget_salary_total,
                    'budget_avaliable_total':budget_avaliable_total,
                    'profit':profit
                    })

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

