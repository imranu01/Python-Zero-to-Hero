a=int(input('enter first number'))
b=int(input("enter second number"))
c=int(input("enter the third number"))
if a>b:
    if a>c:
        print("A is greatest")
elif b>a:
    if b>c:
        print("b is greatest")
    else:
     print("c is greatest")
"""another way to find largest of three"""

if a>b and a>c:
   print("a is greatest")
elif b>a and b>c:
   print("b is greatest")
else:
   print("c is greates")