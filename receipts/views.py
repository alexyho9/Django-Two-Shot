from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from receipts.forms import ReceiptForm
from django.contrib.auth.decorators import login_required


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_list": receipts,
    }
    return render(request, "receipts/list.html", context)


@login_required
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "category_list": categories,
    }
    return render(request, "receipts/by_category.html", context)


@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        "account_list": accounts,
    }
    return render(request, "receipts/by_account.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()
    context = {
        "receipt_form": form,
    }
    return render(request, "receipts/create.html", context)
