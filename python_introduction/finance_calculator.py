income = int(input("Enter your monthly income:"))
expenses = int(input('Enter your total monthly expenses:'))
monthly_savings = income - expenses
interest = 0.05
projected_savings = monthly_savings * 12 + 12 * 0.05 * monthly_savings
print('Your monthly savings are', monthly_savings)
print('Projected savings after one year, with interest, is:', projected_savings)