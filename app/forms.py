from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from app.models import Account, Budget, Expense

from django.core.validators import MaxValueValidator, MinValueValidator

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2' )


# change username for email if needed
class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'username', )

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email {} is already in use.'.format(account))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username {} is already in use.'.format(username))

# Budget forms
class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ('year', 'month', )
        #fields = '__all__'

class ExpenseForm(forms.ModelForm):
    date_time = forms.DateTimeField(input_formats=["%Y-%m-%d %H:%M"])
    amount =  forms.DecimalField(validators=[MinValueValidator(0.0)])

    class Meta:
        model = Expense
        fields = ('expense_type', 'description', 'amount','date_time')