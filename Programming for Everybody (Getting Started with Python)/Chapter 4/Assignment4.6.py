#code below works fine

def computepay(hrs,rt):
    if (hrs > 40):
        pt = 40 * rt + (hrs - 40) * rt * 1.5
    else:
        pt = hrs * rt
    return pt

hrs = float(input("Enter hours: "))
rt = float(input("Enter rate: "))
p = computepay(hrs,rt)
print("Pay",p)
