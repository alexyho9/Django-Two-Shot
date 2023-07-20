from django.forms import ModelForm
from receipts.models import Receipt, ExpenseCategory, Account


class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = [
            "vendor",
            "total",
            "tax",
            "date",
            "category",
            "account",
        ]


class CategoryForm(ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = [
            "name",
        ]


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            "name",
            "number",
        ]
