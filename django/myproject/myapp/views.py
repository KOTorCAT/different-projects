from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def item_detail(request, item_id):
    return render(request, 'myapp/item_detail.html', {'item_id': item_id})