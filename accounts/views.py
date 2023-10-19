from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import customer, transactions
from django.urls import reverse

def home(request):
    customers = customer.objects.all()
    return render(request, 'accounts/dashboard.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def customers(request):
    allcus = customer.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')
        semail = request.POST.get('semail')
        amt = request.POST.get('amt')
        try:
            amt = int(amt)
        except ValueError:
            print("Enter a valid amount")
        for i in allcus:
            if i.email == email:
                j = i
                id = i.id
                break
        for i in allcus:
            if i.email == semail and amt < i.avail_bal and amt > 0:
                avail_bal = i.avail_bal - amt
                avail_bal2 = j.avail_bal + amt
                try:
                    query1 = transactions(name=i.name, email=i.email,
                                          debit=amt, credit=0, acbal=avail_bal)

                    query2 = customer(id=i.id, avail_bal=avail_bal, email=i.email,
                                      name=i.name)
                    query3 = transactions(name=j.name, email=j.email,
                                          debit=0, credit=amt, acbal=avail_bal2)
                    query4 = customer(id=id, avail_bal=avail_bal2, email=j.email,
                                      name=j.name)
                    query2.save()
                    query1.save()
                    query4.save()
                    query3.save()
                    return HttpResponseRedirect(reverse('customers'))
                except Exception as e:
                    print("Transaction failed:", str(e))
        else:
            print("Invalid data")

    return render(request, 'accounts/customers.html', {'list': allcus})

def transaction(request):
    trans = transactions.objects.all()
    return render(request, 'accounts/transactions.html', {'trans': trans})
