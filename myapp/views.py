from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    # for index_old.html
    # context = {
    #     'name': 'Patrick',
    #     'age': 23,
    #     'nationality': 'Indonesian'
    # }
    # return  render(request, 'index.html',context)

    # For manual input. Superseded by using Django Models
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.is_true = True
    # feature1.details = 'Our serivce is OP'

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Mega Fast'
    # feature2.is_true = True
    # feature2.details = 'Our serivce is Mega OP'

    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Mega Fast'
    # feature3.is_true = True
    # feature3.details = 'Our serivce is Mega OP'

    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'Mega Fast'
    # feature4.is_true = False
    # feature4.details = 'Our serivce is Mega OP'

    # feature5 = Feature()
    # feature5.id = 4
    # feature5.name = 'Mega Fast'
    # feature5.is_true = True
    # feature5.details = 'Our serivce is Mega OP'

    # features = [feature1, feature2, feature3, feature4, feature5]

    # Get all objects from Feature -> all the data like name and details!
    features= Feature.objects.all()

    return render(request, 'index.html', {'features': features})

def counter(request):
    words = request.POST['words'] ##Must have POST if using form method POST. GET if GET
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amount': amount_of_words})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists(): #Filter the DB to check if the email is already registered
                messages.info(request, 'Email already used!') #Requests is used to send response
                return redirect('register')
            elif User.objects.filter(username=username).exists(): #Filter the DB to check if the username is already registered
                messages.info(request, 'Username already used!') #Requests is used to send response
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password not the same!') #Requests is used to send response
            return redirect('register')
    else:
        return render(request, 'register.html')
        
def login(request):
    if request.method == 'POST': #check if thisi is after user submit data or not
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None: #if user is registered
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid') 
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
    