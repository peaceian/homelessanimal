from django.shortcuts import render
import requests
import json
from json import load

import math
import  urllib.parse

 
def search(request,animal_kind):
    print('123')
    animal_kind1 = request.form.get('animal_kind')
    print(animal_kind+"1")

    


    animal_kind2 = animal_kind1.encode("UTF-8")
    
    #print(select)
    #animal_sex = request.GET.get('aniaml_sex')
    #top = request.GET.get('top')
    if animal_kind2 == '狗':
        print(animal_kind1+"2")
        #url = f'https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&$top=10&$skip=0'
        url = f'https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&animal_kind={animal_kind2}'
        #decoded_url = urllib.parse.unquote(url)
        
        response = requests.get(url)
        try:
            response = requests.get(url)
        except NameError:
            print('NameError')
        except IndexError:
            print('IndexError')
        except SyntaxError:
            print('SyntaxError')
        except ValueError:
            print('ValueError')
        except AssertionError:
            print('AssertionError')
        except KeyError:
            print('KeyError')
        except AttributeError:
            print('AttributeError')
        except IOError:
            print('IOError')
        except UnboundLocalError:
            print('UnboundLocalError')
        print('其他原因')
        


        data = response.json()
        print(data+"3")
        
        animal_kind = data[0]['animal_kind']
        print(animal_kind+"4")
        #info = url.text
        #jd = json.loads(info)
        #animal_place=[]

        #for item in jd:
        #    animal_place.append(item['animal_place'])
        
    
    elif animal_kind2 =='貓':
        #url = f'https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&animal_kind={select}'
        url = f'https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&animal_kind=%E8%B2%93&%24top=5'
        #decoded_url = urllib.parse.unquote(url)
        response = requests.get(url)
        print(response)
        data = response.json()
        animal_kind = data[0]['animal_kind']
    
    else:
        url = f'https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&animal_kind={animal_kind2}'
        #decoded_url = urllib.parse.unquote(url)
        response = requests.get(url)
        data = response.json()
        animal_kind = data[0]['animal_kind']


    context = {'animal_kind': animal_kind}
    #for item in data:
    #    animal_kind.append(item['animal_kind'])

    return render(request,'animalpage.html',context)
