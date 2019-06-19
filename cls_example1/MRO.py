class X: 
	pass 
class Y: 
	a = -42 
class Z:
	a = 0 

class A(X,Y):
    pass 
class B(Y,Z):
    pass 

class M(B,A,Z):
   	pass 

print(M.mro())
print(M.a)

