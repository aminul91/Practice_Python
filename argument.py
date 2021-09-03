class Product():
    def __init__(self):
         print("product")
    
    def greet_me(self,**kwargs):
        print(kwargs)
        for key, value in kwargs.items():
            print("{0} = {1}".format(key, value))


mall_obj = Product()

mall_obj.greet_me(name="yasoob",address="bamberg",status="student")

        
