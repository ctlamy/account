from django.db import models

# Create your models here.
class Entry(models.Model):
	category_choices = (('S','Sale'),('COGS','CostOfGoodsSold'),('Sal','Salaries'),('R','Rent'))
	se_choices = (('S','Sale'),('E','Expense'))

	se = models.CharField(max_length=1,choices=se_choices)
	category = models.CharField(max_length=16,choices=category_choices)
	name = models.CharField(max_length=16)
	date = models.DateField()
	desc = models.CharField(max_length=128)
	amount = models.DecimalField(max_digits=19,decimal_places=2)
