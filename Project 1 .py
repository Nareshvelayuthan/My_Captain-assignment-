#radius of the circle
radius = float(input("Enter the radius:"))
#area of circle for entered radius
area = 3.14*(radius**2)
print("The area of the circle with radius",radius," is",area)




#input filename and displaying extension as output
filename = input("Input the Filename: ")
f_extns = filename.split(".")
x=f_extns[-1]
dictn={'py':'python','txt':'text','doc':'word','xlsx':'excel','jpg':'jpeg image','mp3':'mp3 audio'}
print(dictn.get(x))
