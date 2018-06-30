import json

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import main
from .forms import TableForm


def tables_list(request):
    table = main.objects.filter(change_date__lte=timezone.now()).order_by('change_date')
    return render(request, 'structure/tables_list.html', {'tables': table})


def table_detail(request, pk):
    # table = get_object_or_404(main, pk=pk)
    print (request)
    if request.method == "POST":
        # print(request.POST)
        # form = TableForm(request.POST)
        # if form.is_valid():
        #     table = form.save(commit=False)
        
        data = json.loads(request.POST.get('table', None))
        # print (data)
        table = main.objects.get(pk=pk)
        # table.editors.add(request.user) 
        # table.create_date = timezone.now()
        table.change_date = timezone.now()
        table.table_body = data
        table.save()
        # print ('saved')
        # return redirect('table_detail', pk=table.pk)
    else:
        table = get_object_or_404(main, pk=pk)
        # request.session['view'] = request.GET['view']
        # return HttpResponse('ok', content_type='text/html')
    # return render(request, 'structure/table_detail.html', {'form': form})
    return render(request, 'structure/table_detail.html', {'table': table})


def table_new(request):
    if request.method == "POST":
        # print(request.POST)
        form = TableForm(request.POST)
        if form.is_valid():
            table = form.save(commit=False)
            
            # data = request.POST.get('table', None)
            # print (data)
            table.owner = request.user
            table.editors.add(request.user) 
            table.create_date = timezone.now()
            table.change_date = timezone.now()
            table.table_body = [
                                    [ {"value":"head 1"}, {"value":"head 2"}, {"value":"head 3"}, {"value":"head 4"}, {"value":"head 5"} ],
                                    [ {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"} ],
                                    [ {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"} ],
                                    [ {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"} ],
                                    [ {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"} ],
                                    [ {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"} ]
                                ]
            table.save()
            return redirect('table_detail', pk=table.pk)
    else:
        form = TableForm()
        # request.session['view'] = request.GET['view']
        # return HttpResponse('ok', content_type='text/html')
    return render(request, 'structure/table_edit.html', {'form': form})

def table_edit(request, pk):
    table = get_object_or_404(main, pk=pk)
    if request.method == "POST":
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            table = form.save(commit=False)
            table.editors.add(request.user) 
            table.change_date = timezone.now()
            table.save()
            return redirect('table_detail', pk=table.pk)
    else:
        form = TableForm(instance=table)
    return render(request, 'structure/table_edit.html', {'form': form})
