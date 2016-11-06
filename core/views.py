# Create your views here.
from django.views.generic.edit import CreateView
from core.models import Entry

class CreateEntry(CreateView):
	template_name = 'entry_input.html'
	
	model = Entry
	fields = ['se', 'category', 'name', 'date', 'desc', 'amount']