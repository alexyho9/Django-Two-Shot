from django.shortcuts import render
from receipts.models import Receipt


# Create your views here.
def receipt_list(request):
    receipts = Receipt.objects.all()
    context = {
        "receipt_list": receipts,
    }
    return render(request, "receipts/list.html", context)
