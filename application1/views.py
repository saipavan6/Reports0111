from django.shortcuts import render
import requests
from datetime import datetime




def index(request):
    response=requests.get('https://bookmyotservice.pythonanywhere.com/GetHospitalList').json()
    return render(request,'Report.html',{'response':response['ResultData']})

def index1(request):
    result = requests.get('https://bookmyotservice.pythonanywhere.com/PhysicianList').json()
    return render(request,'Physician.html',{'result':result['ResultData']})

def index2(request):
    result1 = requests.get('https://bookmyotservice.pythonanywhere.com/AllOTDetails').json()
    return render(request, 'Surgery.html',{'result1':result1['ResultData']})

def index4(request):
    result = requests.get('http://127.0.0.1:9470/AppReports?Id=1').json()
    return render(request, 'View.html',{'result':result['ResultData']})


# def index2(request):
#     api_url = 'https://bookmyotservice.pythonanywhere.com/AllOTDetails'
#     response = requests.get(api_url)

#     api_str = response.json()['datetime']

#     api_datetime = datetime.fromisoformat(api_str)
#     date = api_datetime.date()
#     time = api_datetime.time()
    
#     context = {'date':date, 'time':time}
#     return render(request, 'Surgery.html',{context['ResultData']})

def index3(request):
    result3 = requests.get('https://bookmyotservice.pythonanywhere.com/GetAllHospitalTransaction?hosid=8').json()
    return render(request,'Transaction.html',{'result3':result3['ResultData']})
