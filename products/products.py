from flask import Blueprint, render_template
from collections import defaultdict
from API.api import GetAllProducts, GetSingleProducts, SuggestProducts
products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static')

@products_bp.route('/products')
def index():
    data = GetAllProducts()
    l = len(data)
    kategorie = data["category"]
    distinct_category = []
    for category in data:
        distinct_category[category["category"].append(category)]
    
    return render_template('products/products.html', length = l, products = data, kategorie = distinct_category)

@products_bp.route('/products/<int:id>')

def getSuggestedProducts(id):
    data = GetSingleProducts(id)
    allproducts = GetAllProducts()
    product = GetSingleProducts(id)
    category = product["category"]
    
    suggested_products = []
    category_products = defaultdict(list)
    for p in allproducts:
        category_products[p["category"]].append(p)
        
        
    for p in category_products[category]:
        if p["id"] != id:
            suggested_products.append(p)
            if len(suggested_products) >= 4:
                break
    
    return render_template("products/detail.html" ,DetailOfOneProduct = data, Suggested_Products = suggested_products, kategorie_produkty = category_products )


      