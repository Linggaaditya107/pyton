n =int(input("masukan nilai n untuk batas deret fibonacci:"))

a,b= 0,1

print("Deret fibonacci hingga ",n, ":")
while a <= n:
    print(a, end="")
    a,b=b,a+b