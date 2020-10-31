#Handling zero division error
def divide(x, y): 
    try:  
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 

divide(3,0)

#Raising error 
def raiserror(x):
	if x > 5:
		raise Exception('x should not exceed 5.\n The value of x was: {}'.format(x))


#Handling raised error
def handlerror(x):
    try:
        raiserror(x)
    except:
        print("You can't enter greater than 5")
        
handlerror(6)