from django.shortcuts import render
import pyrebase
from email.message import EmailMessage
import ssl
import smtplib
import requests as req
import json
import random

config ={
    "apiKey": "AIzaSyB7x88N6q8Mq4glPuJk15xoGuiV1d4EPWQ",
    "authDomain": "cecs-443.firebaseapp.com",
    "databaseURL": "https://cecs-443-default-rtdb.firebaseio.com",
    "projectId": "cecs-443",
    "storageBucket": "cecs-443.appspot.com",
    "messagingSenderId": "854450518805",
    "appId": "1:854450518805:web:54c75b726708fdd3a8471c"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
max_spots = 15
def index(request):
    return render(request, 'parking_manager/index.html')

def payment(request):
    if request.method == 'POST':
        print(request.POST['Card_Num'])
        return render(request, 'parking_manager/pages/res_confirmation.html')
    return render(request, 'parking_manager/pages/payment.html')


def res_cancel_confirmation(request):
    return render(request, 'parking_manager/pages/res_cancel_confirmation.html')

def res_cancellation(request):
    if request.method == 'POST':
        code = request.POST['Code']
        pin = request.POST['PIN']
     
        if not database.child(code).shallow().get().val() or code == "":
            print("users does not exist")
        else:
            print("users exist")
            pin_in_db = str(database.child(code).child('Pin Number').get().val())
            print(pin_in_db, type(pin_in_db))
            print(pin, type(pin))
            if pin_in_db != pin:
                return render(request, 'parking_manager/pages/res_modification_rejection.html')
            database.child(code).remove()
            return render(request, 'parking_manager/pages/res_cancel_confirmation.html')
    return render(request, 'parking_manager/pages/res_cancellation.html')

def res_confirmation(request):
    return render(request, 'parking_manager/pages/res_confirmation.html')

def res_mod_confirmation(request):
    return render(request, 'parking_manager/pages/res_mod_confirmation.html')

def res_modification(request):
    if request.method == 'POST':
        code = request.POST['Code']
        pin = request.POST['PIN']
     
        if not database.child(code).shallow().get().val() or code == "":
            print("users does not exist")
        else:
            print("users exist")
            pin_in_db = str(database.child(code).child('Pin Number').get().val())
            print(pin_in_db, type(pin_in_db))
            print(pin, type(pin))
            if pin_in_db != pin:
                return render(request, 'parking_manager/pages/res_modification_rejection.html')
            database.child(code).remove()
            return render(request, 'parking_manager/pages/res_modification_detail.html')
    return render(request, 'parking_manager/pages/res_modification.html')

def reservation(request):
    x = database.child().get().val()
    dates = list(x.values())
    current_spots = len(dates)
    list_dates = []
    for i in dates:
        list_dates.append(i['Date'])
    if request.method == 'POST':
        #print(request.POST['First_Name'])
        ln = request.POST['Last_Name']
        email = request.POST['Email']
        pn = request.POST['Park_Num']
        li = request.POST['License']
        fn = request.POST['First_Name']
        year = request.POST['Year']
        month = request.POST['Month']
        day = request.POST['Day']

        card_num = request.POST['Card_Num']
        cyear = request.POST['Card_Y']
        cmonth = request.POST['Card_M']
        cday = request.POST['Card_D']
        
        date = str(month) + "/" + str(day) + "/" + str(year)
        cdate = str(cmonth) + "/" + str(cday) + "/" + str(cyear)
        # h = hash(date + str(pn)) 
        ch = str(month) +str(day)  + str(year) + str(pn)

        valiDATE(date)

        if not database.child(ch).shallow().get().val():
            parking_pin = random.randint(1000,9999)
            pay = {'Card_Num': card_num, 'EXP': cdate}
            data = {'First_Name': fn , 'Last_Name': ln, 'Date': date, 'Email' : email, 'License' : li, 'Payment' : "",
                    'Park_Num': pn, 'Pin Number': parking_pin, 'Payment': pay}
            beef = 0
            
            for i in list_dates:
                if i == date:
                    beef+= 1
                    print(beef)
            if beef >= max_spots -1:
                return render(request, 'parking_manager/pages/res_rejection_lotful.html')
                
            
            
            database.child(ch).set(data)
            print("hmm")
            
            sendConf(email, ch, parking_pin)
            return render(request, 'parking_manager/pages/res_confirmation.html')
        else:
            print("Already taken")
            return render(request, 'parking_manager/pages/res_rejection_spottaken.html')
    return render(request, 'parking_manager/pages/reservation.html')

def is_spot_taken(date, spot):
    return

def res_modification_detail(request):
    if request.method == 'POST':
        x = database.child().get().val()
        dates = list(x.values())
        current_spots = len(dates)
        list_dates = []
        for i in dates:
            list_dates.append(i['Date'])
        if request.method == 'POST':
            #print(request.POST['First_Name'])
            ln = request.POST['Last_Name']
            email = request.POST['Email']
            pn = request.POST['Park_Num']
            li = request.POST['License']
            fn = request.POST['First_Name']
            year = request.POST['Year']
            month = request.POST['Month']
            day = request.POST['Day']

            card_num = request.POST['Card_Num']
            cyear = request.POST['Card_Y']
            cmonth = request.POST['Card_M']
            cday = request.POST['Card_D']
            
            date = str(month) + "/" + str(day) + "/" + str(year)
            cdate = str(cmonth) + "/" + str(cday) + "/" + str(cyear)
            # h = hash(date + str(pn)) 
            ch = str(month) +str(day)  + str(year) + str(pn)

        valiDATE(date)

        if not database.child(ch).shallow().get().val():
            parking_pin = random.randint(1000,9999)
            pay = {'Card_Num': card_num, 'EXP': cdate}
            data = {'First_Name': fn , 'Last_Name': ln, 'Date': date, 'Email' : email, 'License' : li, 'Payment' : "",
                    'Park_Num': pn, 'Pin Number': parking_pin, 'Payment': pay}
            beef = 0
            
            for i in list_dates:
                if i == date:
                    beef+= 1
                    print(beef)
            if beef >= max_spots -1:
                return render(request, 'parking_manager/pages/res_rejection_lotful.html')
                
            
            
            database.child(ch).set(data)
            print("hmm")
            
            sendConf(email, ch, parking_pin)
            return render(request, 'parking_manager/pages/res_mod_confirmation.html')
        else:
            print("Already Taken")
            return render(request, 'parking_manager/pages/res_modification_detail.html')
    return render(request, 'parking_manager/pages/res_modification_detail.html')

def view_parking_request(request):
    return render(request, 'parking_manager/pages/view_parking_request.html')

def view_parking(request):
    return render(request, 'parking_manager/pages/view_parking.html')
def sendConf(email, hsh, pin):
        sender = "hankbank891@gmail.com"
        password = "tpdb eteh qcdx spep"
        receiver = email
        subject = "Your Reservation is Complete"
        body = 'confirmation number: ' + hsh + '\npin:' + str(pin)
        em = EmailMessage()
        em['From'] = sender
        em['To'] = receiver
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, em.as_string())

def valiDATE(date):
    x = database.child().get().val()
    print(x)

