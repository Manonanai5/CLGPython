money_start = float(input("Enter the starting amount of money: "))
saving_years = int(input("Enter the number of years you plan to save: "))
interest_rate = float(input("Enter the interest rate (e.g., 0.05 for 5%): "))

money_result = money_start + (money_start * interest_rate * saving_years)

print(f"The accumulated savings after {saving_years} years is: {money_result}")

if money_result > 10000:
    print(True)
else:
    print(False)