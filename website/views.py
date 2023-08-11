from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm, AddRecord
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
    
    # check to see if logging in 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been loged in ")
            return redirect('home')
        else:
            messages.success(request, "There is Error in login please try again")
            return redirect('home')
    else:
        return render(request,'home.html', {'records' :records})
   


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')



def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and login 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, " You have succesfully logedin! Welcome")
            return redirect('home') 
    else:
        form = SignUpForm()    
        return render(request, 'register.html',{'form':form})
    
    return render(request, 'register.html',{'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        # look Up Record 
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html',{'customer_record':customer_record})
    else: 
        messages.success(request, "You must be Logged in to view that page..")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, " Record Deleted Sucessfully ")
        return redirect('home')
    else: 
        messages.success(request," You Must Be Logged In ")
        return redirect('home')
    


def add_record(request):
    form = AddRecord(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added..")
                return redirect('home')
            
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Must be Logged in ")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecord(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')