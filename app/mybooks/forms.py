# from django import forms
# from mybooks.models import UserBooks

# class UserBookForm(forms.ModelForm):
#     class Meta:
#         model = UserBooks
#         fields = ['book', 'status', 'resume']

from django import forms
from mybooks.models import UserBooks

class UserBookForm(forms.ModelForm):
    class Meta:
        model = UserBooks
        fields = ['status']