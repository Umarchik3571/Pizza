from django.shortcuts import render
from .models import Pizza, Order


def home(request):
    all_pizza = Pizza.objects.all()

    context = {
        "all_pizza": all_pizza
    }

    return render(request, 'home.html', context=context)