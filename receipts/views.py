from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_list": receipts,
    }
    return render(request, "receipts/list.html", context)
