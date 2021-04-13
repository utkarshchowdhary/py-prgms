def computepay(h, r):
    res = None
    if h <= 40:
        res = h * r
    elif h > 40:
        res = 40 * r + (h - 40) * 1.5 * r
    return res


hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter rate per hour:")
r = float(rph)

p = computepay(h, r)
print("Pay", p)

# Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
