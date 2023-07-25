from management.product_handler import *
from menu import products
from management.tab_handler import *

if __name__ == "__main__":
    
    print(get_product_by_id(32))
    print(get_products_by_type("fruit"))

    test = {
        "title": "Bolinho Python",
        "price": 1.0,
        "rating": 2,
        "description": "Bolinho de Python com chocolate",
        "type": "bakery"
    }

    print(add_product(products, **test))

    print(calculate_tab([
                    {"_id": 10, "amount": 3},
                    {"_id": 20, "amount": 2},
                    {"_id": 21, "amount": 5},
                ]))
    print(menu_report())