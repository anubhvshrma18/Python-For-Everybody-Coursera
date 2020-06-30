#code below works fine

hrs = float(input("Enter hours: "))
rt = float(input("Enter rate: "))
if (hrs > 40):
    p=40 * rt + (hrs-40) * rt * 1.5
else :
    pt = hrs * rt
print(p)
