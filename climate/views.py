import requests
import time
from django.shortcuts import render

def getAPPID():
    return "481e3bc28e5264e5607c2b65b449bfc1";                      #apikey or appid for authorize

response = {}                                                       #Pass variable to template(after render)
def index(request):                                                 #Basically main class in django
    html = 'index.html'
    response['city'] = request.GET.get('loc')                       #show which variable need to pass to template

    if response['city'] == 'Jakarta':                               #Selected city affect to response[data] which is
        response['data'] = getDataJSON('Jakarta','ID')              #used by template table

    elif response['city'] == 'Tokyo':
        response['data'] = getDataJSON('Tokyo','JP')

    elif response['city'] == 'London':
        response['data'] = getDataJSON('London','US')
    
    return render(request, html, response)                          #render html and response

def getDataJSON(cityName,countryCode):
    URL =  'http://api.openweathermap.org/data/2.5/forecast/daily'  #Get api and param url
    PARAMS = {
        'appid' : getAPPID(),                                       #Add this param for authorize
        'q' : cityName + ',' + countryCode,
        'cnt' : 5
    }
    r = requests.get(url = URL, params=PARAMS)                      #Get json data from authorized url
    json = r.json()                                             
    jsonElem = json['list']                                         #As the json is dictionary, specific it into list
                                                                    #using key
    data = []                                                       #Used for formated-json
    for element in jsonElem:
        data.append(formatting(element))                            #format time,temp and variance

    return data

def convertTime(dt):
    return time.strftime('%Y-%m-%d', time.localtime(dt))            #Convert epoch time into formated time

def formatting(data):
    newJson = {}
    #Time
    realTime = convertTime(data['dt'])                              #Convert epoch time
    newJson['time'] = realTime                                      #Add time as key with realTime as value to variable

    #Temperature
    tempCelcius = data['temp']['day'] - 273.15                      #Convert kelvin into celcius
    formatTemp = "{:.1f}".format(tempCelcius)                       #Using only 1 Decimal after comma       
    newJson['temp'] = formatTemp

    #Variance
    minTemp = data['temp']['min']
    maxTemp = data['temp']['max']
    formatVar = "{:.1f}".format(maxTemp-minTemp)                    #Using only 1 Decimal after comma 
    newJson['variance'] = formatVar

    return newJson                                                  #return formatted-json, and pass to template

