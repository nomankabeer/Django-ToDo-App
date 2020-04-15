from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoModule
import datetime
from django.shortcuts import redirect

# Create your views here.

def index(request):
    dataStored = request.session.get('dataStored')
    if dataStored == True :
        data = {'status' : 'true' , 'message' : 'Data is Stored Sucessfully'}
    elif dataStored == False :
        data = { 'status': request.session.get('dataStored') , 'message' : 'Something went wrong'}
    else:
        data = None

    listData = ToDoModule.objects.all()
    context = {'listData' : listData}
    return render(request, 'TodoModule/index.html' , context)

def storeData(request):
    text = request.POST['text']
    now = datetime.datetime.now()
    data = ToDoModule(text=text , pub_date=now)
    if data.save():
        request.session['dataStored'] = True
    return redirect('/')
    
def deleteAll(request):
    ToDoModule.objects.all().delete()
    return redirect('/')

def deleteSelected(request):
    if 'ids[]' in (dict(request.POST)) :
        ids = (dict(request.POST)["ids[]"])
        ToDoModule.objects.filter(id__in=(ids)).delete() # query
    return redirect('/')

def delete(request , id):
    ToDoModule.objects.get(id=id).delete()
    return redirect('/')

def update(request , id):
    text = ToDoModule.objects.get(id=id)
    text.text = request.POST['text']
    text.save()
    return redirect('/')