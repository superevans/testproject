from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Patrick',
        'age': 23,
        'nationality': 'Indonesian'
    }
    return  render(request, 'index.html',context)

def counter(request):
    words = request.POST['words'] ##Must have POST if using form method POST. GET if GET
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amount': amount_of_words})