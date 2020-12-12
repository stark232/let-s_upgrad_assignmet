#split function 
print("1) Using split function of string :")
name=input("Enter your full name :")
name=name.split()
print("First name = "+name[0]+"\nFather's name = "+name[1]+"\nLast name = "+name[2])


#capitalize function 
print("\n\n2)Using capitalize function :")
cap=input("Enter your name :")
cap=cap.capitalize()
print(cap)


#Count function 
print("\n\n3)using count function :")
s=input("Enter any string :")
c=input("Enter the alphabate you want to count ")
ans=s.count(c)
ans=str(ans)
print(c+" occured "+ans+" times")


#find function 
print("\n\n4)Using find function :")
txt="hello , welcome to the school"
num=txt.find("welcome")
if num>=0 :
    num=str(num)
    print("welcome is at "+num+"th position ")
else:
    print("welcome is not present in text")
    
    
#isalpha function
print("\n\n5)Using find function :")
txt="WelcomeHome"
op=txt.isalpha()
print(op)