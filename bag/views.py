from django.shortcuts import render

# Create your views here.

def view_bag(request):
    "View to show users products in their bag"

    return render(request, 'bag/bag.html')