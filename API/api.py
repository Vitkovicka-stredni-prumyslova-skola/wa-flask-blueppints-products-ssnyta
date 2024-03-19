from flask import Blueprint, render_template
import requests

import json


api_bp = Blueprint('api_bp', __name__)
URL_API = "https://fakestoreapi.com"

#Načte  seznam produktů z API v JSON formátu a vrátí jej jako pole.
def GetAllProducts():   
    
    request = requests.get(f"{URL_API}/products")
    
    return json.loads(request.text)

#Načte  seznam produktů z API v JSON formátu a vrátí jej jako pole.
def GetSingleProducts(id):   
    
    request = requests.get(f"{URL_API}/products/" + str(id))
    return json.loads(request.text)
 
def SuggestProducts():
    request = requests.get(f"{URL_API}/products/categories")
    return json.loads(request.text)

def GetMaxID():
    request = requests.get(f"{URL_API}/products")
    data = json.loads(request.text)
    id_produktu = [item["id"] for item in data]
    delka_pole = max(id_produktu)
    return delka_pole
