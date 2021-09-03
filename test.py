try:
    x=float(input())
    y=float(input())
except ValueError:
    print("please provide correct value as input")
finally:
    try:
        z = x/y
        print(z)
    except ZeroDivisionError:
        print("dont devide by zero")
    
    except NameError:
        print("Define all variable and provide value please")

    except Exception as e:
        print(e)

    finally:
        print("Bye")


from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

val = URLValidator(verify_exists=False)
try:
    val('http://www.google.com')
except ValidationError as  e:
    print e


##init func

class Person:  
      
    # init method or constructor   
    def __init__(self,p,q):  

        print(p*q) 

if __name__ == "__main__":
    p = Person(5,6)  

