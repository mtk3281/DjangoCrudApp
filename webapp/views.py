from django.shortcuts import render,redirect
from .forms import CreateRecordForm, UpdateRecordForm

from django.contrib.auth.decorators import login_required
from .models import record


def home(request):
    return render(request, 'index.html')

@login_required(login_url='my-login')
def dashboard(request):
    my_records = record.objects.filter(author=request.user)  # Filter records by the logged-in user
    context = {'records': my_records}
    return render(request, 'dashboard.html', context=context)


@login_required(login_url='my-login')
def create_record(request):
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.author = request.user  # Set the author to the current user
            new_record.save()
            return redirect('dashboard')
    else:
        form = CreateRecordForm()  # Initialize the form for GET requests

    return render(request, 'webapp/create-record.html', {'form': form})



@login_required(login_url='my-login')
def update_record(request, pk):
    rec = record.objects.get(id=pk)
    form = UpdateRecordForm(instance=rec)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST,instance=rec)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {'form' : form}
    return render(request, 'webapp/update-record.html', context=context)


@login_required(login_url='my-login')
def view_record(request, pk):
    all_records = record.objects.get(id=pk)
    
    # Check if the logged-in user is the author of the record
    if all_records.author != request.user:
        return redirect('dashboard')  # Redirect if they are not the author
    
    return render(request, 'webapp/view-record.html', {'record': all_records})


@login_required(login_url='my-login')
def delete_record(request, pk):

    all_records = record.objects.get(id=pk)
    all_records.delete()    
    return redirect('dashboard')