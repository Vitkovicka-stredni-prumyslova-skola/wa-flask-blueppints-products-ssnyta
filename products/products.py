from flask import Blueprint, render_template
from collections import defaultdict

from API.api import GetAllProducts, GetSingleProducts, SuggestProducts
products_bp = Blueprint('products_bp', __name__)

@products_bp.route('/products')
def index():
    data = GetAllProducts()
    all_categories = SuggestProducts()

    l = len(data)
    return render_template('products/products.html', length = l, products = data, kategorie = all_categories)

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
#potřebuji dodělat 
@products_bp.route("/products-category")
def ShowProductsByCategory():
    data = GetAllProducts()
    category = SuggestProducts()
    products_by_cate = []
    
    for p in data:
        if p["category"] == category:
            products_by_cate.append(p)
    return render_template("products/products_cat.html", products = products_by_cate, category = category)

@products_bp.route("/products/add")
def AddProduct():
    all_categories = SuggestProducts()
    return render_template ("products/new_product.html", categories = all_categories)