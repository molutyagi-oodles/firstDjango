from django.shortcuts import render, reverse
from django.http import HttpResponse

# Sample list of product details (in a real application, this would likely come from a database)
PRODUCTS_DATA = [
    {'id': 1, 'name': 'Laptop Pro X', 'price': 1299.99, 'description': 'Powerful laptop for professionals.'},
    {'id': 2, 'name': 'Wireless Mouse Ergonomic', 'price': 29.99, 'description': 'Comfortable wireless mouse with ergonomic design.'},
    {'id': 3, 'name': 'Mechanical Keyboard RGB', 'price': 99.99, 'description': 'High-quality mechanical keyboard with customizable RGB lighting.'},
    {'id': 4, 'name': '4K Monitor 27-inch', 'price': 399.99, 'description': 'High-resolution 4K monitor for crisp visuals.'},
    {'id': 5, 'name': 'Bluetooth Headphones Noise-Cancelling', 'price': 149.99, 'description': 'Premium Bluetooth headphones with active noise cancellation.'},
]

def shop(request):
    return render(request, 'shopApp/shop.html')

def product_list(request):
    context = {'products': PRODUCTS_DATA}
    return render(request, 'shopApp/product_list.html', context)

def product_details(request, product_id):
    try:
        product = next(item for item in PRODUCTS_DATA if item['id'] == product_id)
        context = {'product': product}
        return render(request, 'shopApp/product_details.html', context)
    except StopIteration:
        return HttpResponse("Product not found.", status=404)
    
