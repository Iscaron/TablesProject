from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Table
from .forms import TableForm


def tables_list(request):
    table = Table.objects.filter(change_date__lte=timezone.now()).order_by('change_date')
    return render(request, 'structure/tables_list.html', {'tables': table})


def table_detail(request, pk):
    table = get_object_or_404(Table, pk=pk)
    return render(request, 'structure/table_detail.html', {'table': table})


def table_new(request):
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            table = form.save(commit=False)
            # table.owner = request.user
            # table.create_date = timezone.now()
            # table.change_date = timezone.now()
            # table.save()
            # return HttpResponse('no', content_type='text/html')
            return redirect('table_detail', pk=table.pk)
    else:
        form = TableForm()
        # request.session['view'] = request.GET['view']
        # return HttpResponse('ok', content_type='text/html')
    return render(request, 'structure/table_new.html', {'form': form})

def table_edit(request, pk):
    table = get_object_or_404(Table, pk=pk)
    if request.method == "POST":
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            table = form.save(commit=False)
            table.editors.add(request.user) #TODO: multiply users
            table.change_date = timezone.now()
            table.save()
            return redirect('table_detail', pk=table.pk)
    else:
        form = TableForm(instance=table)
    return render(request, 'structure/table_edit.html', {'form': form})