from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Table

# Table.objects.filter(published_date__lte=timezone.now()).order_by('change_date')

# Create your views here.

#Table.objects.get(pk=pk)


def tables_list(request):
    table = Table.objects.filter(change_date__lte=timezone.now()).order_by('change_date')
    return render(request, 'structure/tables_list.html', {'tables': table})

def table_detail(request, pk):
    table = get_object_or_404(Table, pk=pk)
    return render(request, 'structure/table_detail.html', {'table': table})