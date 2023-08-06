# Define a function that takes a monthly income as a parameter
def income_growth(monthly_income):
    # Initialize the annual income as the monthly income times 12
    annual_income = monthly_income * 12
    # Initialize a list to store the annual income for each year
    income_list = [annual_income]
    # Initialize a variable to store the total income
    total_income = annual_income
    # Loop for x years
    for i in range(8):
        # Increase the annual income by 3 percent
        annual_income = annual_income * 1.03
        # Round the annual income to two decimal places
        annual_income = round(annual_income, 2)
        # Append the new annual income to the list
        income_list.append(annual_income)
        # Add the new annual income to the total income
        total_income += annual_income
    # Return the list of annual incomes and the total income
    return income_list, total_income

# Ask the user to input a monthly income
user_income = float(input("Enter your monthly income: "))
# Call the function with the user input and print the result
print(income_growth(user_income))
