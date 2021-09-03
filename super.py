class Product():
    def __init__(self):
        print("product")

class Shop():
    def __init__(self):
        print("shop")

class Mall(Product,Shop):
    def __init__(self):
        print("mall")
        Product.__init__(self)
        Shop.__init__(self)
mall_obj = Mall()



        
