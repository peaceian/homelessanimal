from django.shortcuts import render
import requests
from json import load
import json
import math
import urllib.parse
import urllib.request
#from django.urls import reverse
#from django.shortcuts import redirect
# web.encoding='utf-8'  #to fix Garbled characters 
# Create your views here.
#from django.http import HttpResponse
#import sys

#def Sayhello(request,username):
#    return HttpResponse("hello"+username)


def animal(request,animal_id):
    api = requests.get('https://data.moa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL') #api connects
    animal_data = api.text
    jd = json.loads(animal_data)  #分析json

    i={} #python dose not initciation

    for oneanimal in jd:
        if animal_id in oneanimal.values():
            #jd=[oneanimal] #define the jd only has a data of target--oneanimal
            #print(jd.value.index(oneanimal))
            i = oneanimal #var i = oneanimal
            
        

    #animal_id=[] #this is not neccessary, the i = oneanimal could import to frontend i.animal_id and so on.
    
    return render(request,"animal.html",locals())
    
    #find the index of oneanimal chosen
    #for oneanimal in jd:
    #    if animal_id in oneanimal.values():
    #        print(jd.index(oneanimal))
    #        i = oneanimal
            
    
#all animals function
def crawlerall(request):
    api = requests.get('https://data.moa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL')
    info = api.text
    jd = json.loads(info)

    animal_id=[]
    animal_place=[]  #建立空串列
    animal_kind=[]
    animal_sex=[]
    animal_bodytype=[]
    animal_colour=[]
    animal_age=[]
    album_file=[]
    animal_update=[]
    shelter_name=[]
    shelter_address=[]
    shelter_tel=[]

    for item in jd:  #將元素添加入串列
        animal_id.append(item['animal_id'])
        animal_place.append(item['animal_place'])
        animal_kind.append(item['animal_kind'])
        animal_sex.append(item['animal_sex'])
        animal_bodytype.append(item['animal_bodytype'])
        animal_colour.append(item['animal_colour'])
        animal_age.append(item['animal_age'])
        album_file.append(item['album_file'])
        animal_update.append(item['animal_update'])
        shelter_name.append(item['shelter_name'])
        shelter_address.append(item['shelter_address'])
        shelter_tel.append(item['shelter_tel'])

    return render(request,"animals.html",locals())



#pages function

page1 = 1
def animalpage(request,pageindex=None):
    global page1
    api = requests.get('https://data.moa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL')
    info = api.text
    jd = json.loads(info)
    animal_place=[]

    for item in jd:
        animal_place.append(item['animal_place'])#use animal_place be a base count

    datasize = len(animal_place)  #資料筆數
    pagesize = 20 #每頁資料筆數，可更換
    totpage = math.ceil(datasize / pagesize)

    if pageindex == None:  #無參數
        page1 = 1
        jds = jd[:pagesize] #取前10筆
    elif pageindex =='1':  #上一頁
        start = (page1-2)*pagesize #該頁的第1筆資料
        if start >=0:  #有前頁資料就顯示
            jds = jd[start:(start+pagesize)]
            page1 -= 1
    elif pageindex == '2':  #下一頁
        start = page1*pagesize
        if start < datasize: #有下頁資料就顯示
            jds = jd[start:start+pagesize]
            page1 = page1 + 1
    elif pageindex == '3': #由詳細頁面返回首頁
        start = (page1-1)*pagesize  #取得原有頁面第1筆資料
        jds = jd[start:start+pagesize]
    currentpage = page1

    return render(request,"animalpage.html",locals())

#filter function

#def filter(request):
#    api = requests.get('https://data.moa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL')
#    info = api.text
#    jd = json.loads(info)
#    jds = jd.objects.filter(animal_kind="貓").values()
#    i = jds
    
    #animal_kind=[]

#    for i in jds:
#        print(i)

#    return render(request,"filter.html",locals)

def search(request):
    if request.method=='POST':
        animal_kind = request.POST['animal_kind']
        print(animal_kind)
        animal_kind = urllib.parse.quote(animal_kind)
        print(animal_kind)

        url = urllib.request.urlopen('https://data.coa.gov.tw/Service/OpenData/TransService.aspx?animal_kind='+animal_kind+'&UnitId=QcbUEzN6E6DL')
        #url = f'https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&animal_kind={animal_kind2}'
        
        info = url.text
        jd = json.loads(info)
        animal_place=[]

        for item in jd:
            animal_place.append(item['animal_place'])#use animal_place be a base count
        
        
        
    
        #elif animal_kind2 =='貓':
        #url = f'https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&animal_kind={select}'
        #url = f'https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&animal_kind=%E8%B2%93&%24top=5'
        #decoded_url = urllib.parse.unquote(url)
        #response = requests.get(url)
        ##print(response)
        #data = response.json()
        #animal_kind = data[0]['animal_kind']
    
    else:
        data = {}
        #url = f'https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&animal_kind={animal_kind2}'
        #decoded_url = urllib.parse.unquote(url)
        #response = requests.get(url)
        #data = response.json()
        #animal_kind = data[0]['animal_kind']


        
    #for item in data:
    #    animal_kind.append(item['animal_kind'])

    return render(request,'animalpage.html',locals)


"""
def search(request,animal_kind):
    print('123')
    animal_kind = request.form.get('animal_kind')
    print(animal_kind+"1")
    animal_kind == '狗'
    print(animal_kind+"2")
    url = f'https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&$top=10&$skip=0'
    response = requests.get(url)
    data = response.json()
    animal_kind = data[0]['animal_kind']
    context = {'animal_kind': animal_kind}
    return render(request,'search.html',context)
"""