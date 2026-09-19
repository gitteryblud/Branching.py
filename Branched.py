# Prompt user for input
kwh = int(input("Enter the KW hours used: "))

# Calculate total cost based on usage threshold
if kwh <= 1000:
    total_cost = kwh * 0.07633
else:
    first_1000_cost = 1000 * 0.07633
    over_1000_cost = (kwh - 1000) * 0.09259
    total_cost = first_1000_cost + over_1000_cost

# Print output matching expected format
print(f"Amount owed is ${total_cost}")
