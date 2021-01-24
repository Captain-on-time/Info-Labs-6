d2 = dict(bananas=3,apples=5,oranges=2,bag="basket") 

d5 = d2.copy() 
print("Dict d5 copying d2 = ", d5) 

print("Get dict value by key d5['bag']: ", d5["bag"]) 
print("Get dict value by key d5.get('bag'): ", d5.get('bag')) 
print("Get dict keys d5.keys(): ", d5.keys()) 
print("Get dict values d5.values(): ", d5.values()) 
print("\n")

myInfo = {
    "surname": "Chekmareva",
    "name": "Arina",
    "middlename": "Vitalevna",
    "day": 8,
    "month": 5,
    "year": 2001,
    "university": "ITMO University"
}
print(myInfo.keys())
print(myInfo.values())