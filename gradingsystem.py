print("Enter the marks that you obtained")
m=int(input("Maths:"))
e=int(input("English"))
s=int(input("science"))
h=int(input("History"))
sum=m+e+s+h
print(sum)
p=sum/4
print(p)
if p>90:
    print("Mastering")
elif p>70:
    print("Achieving")
elif p>50:
    print("Approaching")
else:
    print("Developing")