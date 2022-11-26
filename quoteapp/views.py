from django.shortcuts import render, redirect
from .models import Actor, Quote
from django.contrib import messages
import random

def HomePage(request):
    all_actors = Actor.objects.all()

    if request.method == 'POST':
        actor_name = request.POST.get('actor_name')
        
        if not actor_name:
            messages.error(request, 'You have to select an actor')
            return redirect('home')

        get_actor = Actor.objects.get(quoter=actor_name)
        get_quotes = Quote.objects.filter(actor=get_actor)

        random_quote = random.choice(get_quotes)

        context = {
            "quote": random_quote,
            "actors": all_actors,
        }
        return render(request, 'index.html', context)
    
    context = {
        "actors": all_actors,
    }

    return render(request, 'index.html', context)
