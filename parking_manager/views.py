from django.shortcuts import render


def index(request):
    user = "John"  # Replace this with your user data
    return render(request, 'parking_manager/index.html', {'user': user})

def payment(request):
    return render(request, 'parking_manager/payment.html')

def res_cancel_confirmation(request):
    return render(request, 'parking_manager/res_cancel_confirmation.html')

def res_cancellation(request):
    return render(request, 'parking_manager/res_cancellation.html')
 
def res_confirmation(request):
    return render(request, 'parking_manager/res_confirmation.html')

def res_mod_confirmation(request):
    return render(request, 'parking_manager/res_mod_confirmation.html')

def res_modification(request):
    return render(request, 'parking_manager/res_modification.html')

def reservation(request):
    return render(request, 'parking_manager/reservation.html')