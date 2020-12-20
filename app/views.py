from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from app.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm, BudgetForm

# flash message
# https://docs.djangoproject.com/en/3.1/ref/contrib/messages/#using-messages-in-views-and-templates
from django.contrib import messages

from .models import Budget

# from django.contrib.auth.decorators import login_required
# @login_required(login_url='login')

def home(request):
    # messages.debug(request, 'SQL statements were executed.')
    # messages.info(request, 'Three credits remain in your account.')
    # messages.success(request, 'Profile details updated.')
    # messages.warning(request, 'Your account expires in three days.')
    # messages.error(request, 'Document deleted.', extra_tags='danger')

    user = request.user
    if user.is_authenticated: 
        return redirect("budgets")

    return render(request, 'app/home.html', {})

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'app/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):

    context = {}

    user = request.user
    if user.is_authenticated: 
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    # print(form)
    return render(request, "app/login.html", context)

# add success message as normal
def account_view(request):

    if not request.user.is_authenticated:
            return redirect("login")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                    "email": request.POST['email'],
                    "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(

            initial={
                    "email": request.user.email, 
                    "username": request.user.username,
                }
            )

    context['account_form'] = form

    return render(request, "app/account.html", context)


def must_authenticate_view(request):
    return render(request, 'app/must_authenticate.html', {})

@login_required(login_url='must_authenticate')
def budgets(request):
    context = {}

    budgets = Budget.objects.filter(user=request.user)
    context['budgets'] = budgets

    form = BudgetForm()
    context['create_budget_form'] = form

    return render(request, 'app/budgets.html', context)


@login_required(login_url='must_authenticate')
def create_budget(request):
    context = {}

    form = BudgetForm()

    if request.method == 'POST':
        form = BudgetForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Budget created')
            return redirect('budgets')
        else:
            messages.error(request, 'Form is invalid')

    #context['create_budget_form'] = form
    return redirect("budgets")
