
car =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}





#get function 
print("\n\n1)using  get function") 
x = car.get("model")
print("value of model n dictionary is " + x)


#items function 
print("\n\n2)using  items function") 
x = car.items()
print(x)

#update function
print("\n\n3)using update function")
car.update({"color": "White"})
print(car)


#values function
print("\n\n4)using values function")
x = car.values()
print(x)

#clear function
print("\n\n5)using  clear function") 
car.clear()
print(car)