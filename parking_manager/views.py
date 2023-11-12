from django.shortcuts import render


def index(request):
    return render(request, 'parking_manager/index.html')

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

def res_modification_detail(request):
    return render(request, 'parking_manager/pages/res_modification_detail.html')

