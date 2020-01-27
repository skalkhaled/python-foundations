cart=[]
def greeting(name):
    print("Hello %s , welcome to Sultan Center" % name)
   
def user_shopping(cart):
    item_name = input("What products did you purchase? ")
    while item_name != "done":
        item_quantity = int(input("How many did you purchase?"))
        item_price = float(input("How much is it for? "))
        # total_price = print(float(item_quantity * item_price) + "KWD")
        item = {
            "name" : item_name,
            "price" : item_price,
            "quantity" : item_quantity
            }
        cart.append(item)
        item_name = input("What products did you purchase? ")

    print()
    print("-----------------")
    print("reciept")
    print("-----------------")
    print()
    total=0.0
    for item in cart:
        print("%d %s %f KWD" %(item['quantity'],item['name'],item['price']))
        total+= (item['quantity']*item['price'])
    print("Total Price: %fKD" % total)

name= input("Your name? ")
greeting(name)

user_shopping(cart)
    