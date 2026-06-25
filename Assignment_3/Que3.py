def predict_output():
    x = 10
    print(x)

predict_output()
print(x) 
# Line number 6 will give Error as the x is not defined 
# And the x from predict_output function has been declared locally 
# so it will have scope only for function.