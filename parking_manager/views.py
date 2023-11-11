from django.shortcuts import render


def index(request):
    user = "John"  # Replace this with your user data
    return render(request, 'parking_manager/index.html', {'user': user})

def payment(request):
    return render(request, 'parking_manager/pages/payment.html')

def res_cancel_confirmation(request):
    return render(request, 'parking_manager/pages/res_cancel_confirmation.html')

def res_cancellation(request):
    return render(request, 'parking_manager/pages/res_cancellation.html')
 
def res_confirmation(request):
    return render(request, 'parking_manager/pages/res_confirmation.html')

def res_mod_confirmation(request):
    return render(request, 'parking_manager/pages/res_mod_confirmation.html')

def res_modification(request):
    return render(request, 'parking_manager/pages/res_modification.html')

def reservation(request):
    return render(request, 'parking_manager/pages/reservation.html')