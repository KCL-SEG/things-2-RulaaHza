# views.py
from django.shortcuts import render, redirect
from .forms import ThingForm
from .models import Thing

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            # Process the valid form data, e.g., save to the database
            form.save()
            return redirect('home')  # Redirect to the home page or any other page
    else:
        form = ThingForm()

    return render(request, 'home.html', {'form': form})
