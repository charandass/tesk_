from django.shortcuts import render, redirect
from .models import Item, Bill

# Create your views here.
def item_list(request):
    items = Item.objects.all()
    return render(request, 'products/items_list.html',{"items":items})

def create_bill(request):
    if request.method == 'POST':
        item_ids = request.POST.getlist('items')
        items = Item.objects.filter(id__in=item_ids)
        if items:
            bill = Bill.objects.create()
            bill.items.set(items)
            bill.save()
            return redirect('bill_detail', bill_id=bill.id)
    else:
        items = Item.objects.all()
    return render(request, 'products/create_bill.html', {'items':items})

def bill_detail(request,bill_id):
    bill = Bill.objects.get(id=bill_id)
    return render(request, 'products/bill_detail.html',{"bill":bill})
    
