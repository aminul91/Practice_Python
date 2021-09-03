def sent_num(): # A function which is generator here
    x=1
    while x<10:
        y=x**2
        x=x+1
        yield y      # a special key word which convert this function as generator
        
if __name__ == "__main__":
    output_obj = sent_num()
    for i in output_obj:
        print(i)
   