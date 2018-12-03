# Assignment requires a mortgage calculator
# Calculate the monthly payment in dollars, as a floating-point number, using the formula
# Formula (p * r(1 + r)^n) / ((1 + r)^n - 1)
# p is the mortgage
# r is the monthly decimal rate
# n is the monthly payments in the payback period
# input values

print("Welcome to My Mortgage Calculator") # show welcome message

p = float(input("What is the purchase amount?")) # user inputs amount

interest = float(input("What is annual interest rate? Ex. 5.1% = 5.1, 10% = 10, etc.")) # user inputs rate

r = (interest/100)/12 # takes annual converts to monthly interest rate by dividing by 100, then by 12

years = float(input("What is the length of the loan in years?")) # user inputs years
n = int(years) * 12 # multiply years and 12 to get total months

c = (p * (1 + r)**n) * r / ((1 + r)**n - 1) # c = assigned formula to calculate monthly mortgage

print('%0.2f' % p, "Dollars Borrowed") # show purchase amount
print(interest, "Percent Annual Interest Rate") # show rate
print('%0.2f' % c, "dollars a month for", int(years), "years") # show monthly mortgage and length of loan
