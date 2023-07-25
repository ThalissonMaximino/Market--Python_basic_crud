from menu import products
from statistics import mode

def get_product_by_id(productId: int): 

    if not type(productId) == int:
        raise TypeError("product id must be an int")   

    for product in products:
        if product["_id"] == productId:
            return product

    return {}
    


def get_products_by_type(food_type:str):

    if not type(food_type) == str:
        raise TypeError("product type must be a str")
    
    new_list = []

    for product in products: 
        if product["type"] == food_type:
            new_list.append(product)
            
        
    return new_list


def add_product(products, **menu: dict):

    if len(products) > 0:
        menu["_id"] = max(product['_id'] for product in products) + 1
        products.append(menu)
    
        return menu

    menu["_id"] = 1
    products.append(menu)
    return menu
   
  
def menu_report():
    count = 0
    price = 0
    common_type = []

    for item in products:
            count +=1
            price += item['price']
            common_type.append(item['type'])

    common_type_aux = mode(common_type)
    price_aux = round(price/count, 2)
    return f"Products Count: {count} - Average Price: ${price_aux} - Most Common Type: {common_type_aux}"