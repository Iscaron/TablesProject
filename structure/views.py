from django.shortcuts import render
from django.utils import timezone
from .models import Table

# Table.objects.filter(published_date__lte=timezone.now()).order_by('change_date')

# Create your views here.

def tables_list(request):
    table = Table.objects.filter(change_date__lte=timezone.now()).order_by('change_date')
    return render(request, 'structure/tables_list.html', {'tables': table})