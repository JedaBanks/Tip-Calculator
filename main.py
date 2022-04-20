print("Welcome to the tip calculator!")
totalbill = float(input("What was the total bill? $"))
tip = input("How much tip would you like to give? 10, 12, or 15? ")
split = int(input("How many people to split the bill? "))
perc = int(tip) / 100
bill = format((totalbill / split) * perc , ".2f")
print(f"Each person should pay: ${bill}")