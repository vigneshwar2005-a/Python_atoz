p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

ci = p * (1 + r / 100) ** t - p

print("Compound Interest =", ci)