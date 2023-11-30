from django.db import models
import requests
import json

# Create your models here.
class AnimalModel(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    item = models.TextField(default='{}')

    def __str__(self):
        return self.name
    
    def get_items_dict(self):
        api = requests.get('http://data.moa.gov.tw/Service/OpenData/AnimalOpenData.aspx?$top={top}&$skip={skip}&$filter={filter}')
        info = api.text
        jd = json.loads(info)
        return jd(self.item)