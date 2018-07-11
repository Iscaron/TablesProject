import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.contrib.auth.models import User


from .forms import TableForm, UserForm, UserProfileForm, EditForm
from .models import Main

@login_required
def tables_list(request):
    table = Main.objects.filter(change_date__lte=timezone.now()).order_by('change_date')
    return render(request, 'structure/tables_list.html', {'tables': table})


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


@login_required
def table_detail(request, pk):
    table = get_object_or_404(Main, pk=pk)
    if request.user not in table.editors.all():
        return HttpResponseRedirect('/')
    if request.method == "POST":
        data = json.loads(request.POST.get('table', None))
        table = Main.objects.get(pk=pk)
        table.change_date = timezone.now()
        table.table_body = data
        table.save()
    else:
        table = get_object_or_404(Main, pk=pk)
    return render(request, 'structure/table_detail.html', {'table': table})


@login_required
def table_new(request):
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            table = form.save(commit=False)
            table.owner = request.user
            table.create_date = timezone.now()
            table.change_date = timezone.now()
            table.table_body = [[ {"value":"head 1"}, {"value":"head 2"}, {"value":"head 3"}, {"value":"head 4"}, {"value":"head 5"} ],
                                [ {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"} ],
                                [ {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"} ],
                                [ {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"} ],
                                [ {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"} ],
                                [ {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"}, {"value":"value"} ]
                                ]
            table.save()
            table.editors.add(request.user) 
            table.save()
            return redirect('table_detail', pk=table.pk)
    else:
        form = TableForm()
    return render(request, 'structure/table_edit.html', {'form': form})


@login_required
def table_edit(request, pk):
    table = get_object_or_404(Main, pk=pk)
    if request.user not in table.editors.all():
        return HttpResponseRedirect('/')
    if request.method == "POST":
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            save_table = form.save(commit=False)
            save_table.editors.clear() # TODO: do without clear()
            for user_id in request.POST.getlist('editors'):
                save_table.editors.add(User.objects.get(pk=user_id))
            save_table.save()
            return redirect('table_detail', pk=table.pk)
    else:
        data = {
                'title': table.title,
                'description': table.description,
                'editors': table.editors.all()
        }
        print(table.editors.all())
        form = EditForm(data)
    return render(request, 'structure/table_edit.html', {'form': form})


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'structure/login.html', {})


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')
