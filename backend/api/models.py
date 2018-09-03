from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=50, blank=False)
    lastname = models.CharField(max_length=50, blank=False)
    idcard = models.CharField(max_length=10, blank=False)
    phone = models.CharField(max_length=20, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('lastname', 'firstname', 'idcard',)
        unique_together = (('id', 'user'),)

    def __str__(self):
        return self.lastname + ', ' + self.firstname + ' - ' + self.idcard


class CurrencyType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=False, default='')
    symbol = models.CharField(max_length=4, blank=False, default='')
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name + ' (' + self.symbol + ')'


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField(editable=False, default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True,
                               related_name='accounts')
    currencyType = models.ForeignKey(CurrencyType, on_delete=models.CASCADE,
                                     null=True, related_name='currencyType')
    currency = models.ForeignKey(CurrencyType, on_delete=models.CASCADE,
                                 null=True, related_name='currency', editable=False)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id', 'number', 'client')
        unique_together = (('client', 'currencyType'),)

    def __str__(self):
        return str(self.number) + ' - ' + self.client.__str__() + ' - ' + self.currencyType.__str__()

    def save(self, *args, **kwargs):
        # Allways same value.
        self.currency = self.currencyType;
        # Autoincrement Number Account
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            exist = Account.objects.all().first()
            if exist is not None:
                # Get the maximum NUMBER value from the database
                last_id = Account.objects.all().aggregate(largest=models.Max('number'))['largest']

                # aggregate can return None! Check it first.
                # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
                if last_id is not None:
                    self.number = last_id + 1
            else:
                self.number = 1

        super(Account, self).save(*args, **kwargs)


class Transfer(models.Model):
    id = models.AutoField(primary_key=True)
    accountFrom = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='accountFrom', null=True)
    accountTo = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='accountTo', null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ('date',)
        unique_together = ('id',)

    def __str__(self):
        return 'Transfer from ' + str(self.accountFrom) + ' to ' + str(self.accountTo)
