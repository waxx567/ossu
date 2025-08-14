# 3.2 is 3.1 with error checking added.

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if h > 40:
    op = (h - 40) * (r * 1.5)
    pay = 40 * r + op
else:
    pay = h * r
print("Pay:", pay)