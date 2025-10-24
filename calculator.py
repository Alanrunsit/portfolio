import math
choice=int(input("Choose one of the following shapes:\n1. Square\n2. Rectangle\n3. Triangle\n4. Circle\n"))

if choice == 1:
  side=int(input("Enter side length: "))
  area=side*side
  print("Area=", area)

elif choice == 2:
  length=int(input("Enter length: "))
  width=int(input("Enter width: "))
  area=length*width
  print("Area=",area)

elif choice == 3:
    base=int(input("Enter base: "))
    height=int(input("Enter height: "))
    area=(base*height)/2
    print("Area= ", area)

elif choice == 4:
    radius=int(input("Enter radius: "))
    area=math.pi*(radius**2)
    print("Area= ", area)

else:
  print("Not a listed option")