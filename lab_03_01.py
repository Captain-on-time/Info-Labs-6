a1 = tuple() 
a2 = 1, 2, 3, "abc" 
a3 = (1, 2, 3, "abc") 
print("Tuple a1 = ", a1) 
print("Tuple a2 = ", a2) 
print("Tuple a3 = ", a3) 

l = [1, 2, 3, "abc"] 
a4 = tuple(l) 
print("Tuple a4 from list l = ", a4) 
a5 = tuple("Hello, World!") 
print("Tuple a5 from string = ", a5) 

a6 = a2, a3 
print("Tuple a6 formed by a2 and a3 = ", a6) 

a7 = a2 + a3 
print("Tuple a7 by combining a2 and a3 = ", a7) 

print("a6[0]: ", a6[0]) 
print("a6[0][3]: ", a6[0][3]) 
print("\n")


k1 = (int(input()), int(input()), int(input()))
k2 = (input(), input(), input())
k3 = k1 + k2
print(k3)

k4 = k1, k2
print(k4)
print(k4[1][1])