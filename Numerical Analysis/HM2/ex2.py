import numpy as np
a = 1
b = 2

for i in range(50):
    t = a
    a = b
    b = a + t
    error = np.float64((1+5**(1/2))/2-b/a)
    print(str(i+1)+'|'+str(b/a)+'|'+str(error))

lambd = (0.00038692992636546464-0.0010136302977241662)/(0.0010136302977241662-0.0026493733652794837)
print('lambda =', lambd)
