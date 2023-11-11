from django.shortcuts import render


def index(request):
    user = "John"  # Replace this with your user data
    return render(request, 'parking_manager/index.html', {'user': user})

def payment():
    return

def res_cancel_confirmation():
    return

def res_cancellation():
    return

def res_confirmation():
    return

def res_mod_confirmation():
    return

def res_modification():
    return

def reservation(request):
    return