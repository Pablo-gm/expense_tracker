import datetime
from decimal import Decimal
from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import MinValueValidator

# based on mitchtabian
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# based on mitchtabian
class Account(AbstractBaseUser):
    email           = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username        = models.CharField(max_length=30, unique=True)
    date_joined     = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    # field to use for login example: email
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    # display username
    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


DEFAULT_USER_ID = 1

# Budget model
class Budget(models.Model):

    # Month options
    class Months(models.IntegerChoices):
        JANUARY = 1, 'January'
        FEBRUARY = 2, 'February'
        MARCH = 3, 'March'
        APRIL = 4, 'April'
        MAY = 5, 'May'
        JUNE = 6, 'June'
        JULY = 7, 'July'
        AUGUST = 8, 'August'
        SEPTEMBER = 9, 'September'
        OCTOBER = 10, 'October'
        NOVEMBER = 11, 'November'
        DECEMBER = 12, 'December'

    YEAR_CHOICES = [(y,y) for y in range(2018, datetime.date.today().year+1)]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    month = models.IntegerField(choices=Months.choices, default=Months.choices[datetime.datetime.now().month - 1])
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,  validators=[MinValueValidator(Decimal('0.00'))])

    @property
    def get_income_total(self):
        expenses = self.expense_set.all()
        total = sum([expense.amount for expense in expenses if expense.expense_type == 'INC'])
        return total 

    def get_expense_total(self):
        expenses = self.expense_set.all()
        total = sum([expense.amount for expense in expenses if expense.expense_type != 'INC'])
        return total 

    def get_category_total(self):
        expenses = self.expense_set.all()
        totals = {}
        for expense in expenses:
            if expense.expense_type == 'INC' or expense.amount < 0:
                continue
            if expense.expense_type not in totals:
                totals[expense.expense_type] = expense.amount
            else:
                totals[expense.expense_type] += expense.amount

        return {k: v for k, v in sorted(totals.items(), key=lambda item: item[1], reverse=True)}

    def get_minimum_datetime(self):
        return datetime.datetime(self.year, self.month, 1)

    # @register.filter
    # def get_expense_category(self, category):
    #     return self.items.filter(expense_type__exact=category)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user','year','month'], name='unique_monthly_budget'),
            ]

# Expenses model
class Expense(models.Model):

    INCOME = 'INC'
    HOUSING = 'HOU'
    TRANSPORTATION = 'TRA'
    FOOD = 'FOO'
    UTILITIES = 'UTL'
    MEDICAL = 'MED'
    SAVINGS = 'SAV'
    PERSONAL = 'PER'
    ENTERTAINMENT = 'ENT'
    EDUCATION = 'EDU'
    GIFTS = 'GIF'

    EXPENSE_CHOICES = [
        (INCOME, 'Income'),
        (HOUSING, 'Housing'),
        (TRANSPORTATION, 'Transportation'),
        (FOOD, 'Food & Groceries'),
        (UTILITIES, 'Utilities'),
        (MEDICAL, 'Medical & Insurance'),
        (SAVINGS, 'Savings'),
        (PERSONAL, 'Personal'),
        (ENTERTAINMENT, 'Entertainment'),
        (EDUCATION, 'Education'),
        (GIFTS, 'Gifts & Donations'),
    ]

    expense_type = models.CharField(
        max_length=3,
        choices=EXPENSE_CHOICES,
        default=FOOD,
    )

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    description = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_time = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=DEFAULT_USER_ID)

