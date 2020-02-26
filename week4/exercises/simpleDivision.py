#define the simple_divide function here
def simple_divide(item, denom):
    try:
       item / denom
    except ZeroDivisionError:
        return (0)
    else:  
       return item / denom 
