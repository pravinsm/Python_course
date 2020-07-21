# Assignment Day_2

#Variables:- Syntax: Variable Name = value

operand1 = 10
operand2 = 2
print("""Arithmetic Operators\n
operand1=%d
operand2=%d"""%(operand1,operand2))
#Addition
operation = operand1 + operand2
print("Addition value = %d"%(operation)) #Escape Sequences
#Subtraction
operation = operand1 - operand2
print("Subtracted value = ",operation)
#Division
operation = operand1//operand2 #Returns Integer(Floor Division)
print("Divided value = ",operation)
#Reminder
operation = operand1 % operand2
print('Reminder\'s value = ',operation) #Back Slash
#Multipliaction
operation = operand1 * operand2
print("Multiplied value = ",operation)

a=10 
b=20.2
print("""\nAssignment Operators and Logical Operators\n
a=%d 
b=%.2f\n"""%(a,b))
print("a>b",a>b)
print("a<b",a<b)
print("a==b",a==b)
print("a!=b",a!=b)#not
print("a<=10",a<=10)
print("b>=20.2",b>=20.2)
print("a>b or a<b",a>b or a<b)#or
print("a>b and a<b",a>b and a<b)#and
print("a<=10 and a<b",a<=10 and a<b)

# Triple Quotes
print ("""\nPython Course is Awesome !
        Thanks Let's Upgrade !!!""")
