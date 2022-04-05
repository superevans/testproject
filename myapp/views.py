from django.shortcuts import render
from django.http import HttpResponse
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