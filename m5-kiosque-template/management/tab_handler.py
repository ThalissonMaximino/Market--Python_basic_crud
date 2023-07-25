from menu import products

def calculate_tab(tab: list):
    bill = 0
    for item in tab:
        for element in products:
            if element['_id'] == item['_id']:
                bill += element['price']*item['amount']
    rounded_bill = round(bill, 2)            
    return {"subtotal": f'${rounded_bill}'}
