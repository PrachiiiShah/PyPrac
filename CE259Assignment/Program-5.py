# Explain about the different types of Exceptions in Python with suitable example

"""1.	exception ArithmeticError
This class is the base class for those built-in exceptions that are raised for various arithmetic errors such as:
•	OverflowError
•	ZeroDivisionError
•	FloatingPointError

try:  
    a = 10/0  
    print (a)
except ArithmeticError:  
        print ("This statement is raising an arithmetic exception.")
else:  
    print ("Success.")


2.	exception LookupError
This is the base class for those exceptions that are raised when a key or index used on mapping or sequence is invalid or not found. The exceptions raised are :
•	KeyError
•	IndexError


try: 
    a = [1, 2, 3] 
    print (a[3]) 
except LookupError: 
    print ("Index out of bound error.")

3.	exception AttributeError
An AttributeError is raised when an attribute reference or assignment fails such as when a non-existent attribute is referenced.

class Attributes(object):
    pass
  
object = Attributes()
print (object.attribute)

4.	exception FloatingPointError
A FloatingPointError is raised when a floating point operation fails. This exception is always defined, but can only be raised when Python is configured with the–with-fpectl option, or the WANT_SIGFPE_HANDLER symbol is defined in the pyconfig.h file.
    

import math
  
print (math.exp(1000))

5.	exception IndexError
An IndexError is raised when a sequence is referenced which is out of range.


array = [ 0, 1, 2 ]
print (array[3])
"""