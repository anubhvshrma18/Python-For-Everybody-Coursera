#code below works fine
largest =0
smallest=0
while True:
    nu = input("Enter a number: ")
    if nu == 'done' :
        break
    try:
        num=int(nu)
    except:
        print("Invalid input")
    if(largest ==0):
        largest=num
    if(smallest == 0):
        smallest=num
    if (num > largest):
        largest = num
    if(num < smallest):
        smallest=num

print("Maximum is",largest)
print("Minimum is",smallest)
