# views.py
from django.shortcuts import render, redirect
from .models import Pen, Store

def add_store_and_pen(request):
    if request.method == 'POST':
        # Get the form data directly from POST
        brand = request.POST.get('brand')
        store_name = request.POST.get('name')
        price = request.POST.get('price')

        # Validation for required fields
        if brand and store_name and price.isdigit():
            # Create the Pen instance
            pen = Pen.objects.create(brand=brand)
            
            # Create the Store instance
            store = Store.objects.create(name=store_name, price=int(price))
            
            # Add the Pen to the Store (ManyToMany relation)
            store.pens.add(pen)
            
            return redirect('index')  # Redirect to the same page after saving
        else:
            error_message = "Please fill all the fields correctly."
            return render(request, 'index.html', {'error_message': error_message})

    return render(request, 'index.html')
