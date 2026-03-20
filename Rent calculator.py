# Rent calculator for Flatmates
#this program calculates how muvh each person should pay

#Get input from the users
rent =int(input("Enter total flat rent:"))
food =int(input("Enter total food/snacks cost:"))
electricity_units=int(input("Enter electricity units used: "))
unit_charge = int(input("Enter charge per electricity unit:"))
persons =int(input("Enter number of persons in the flat:"))

#calculate electricicty cost
electricity_total = electricity_units * unit_charge

#calculate total expenses 
total_expense=rent + food+ electricity_total

#calculater share per person
per_person=total_expense/persons

#show the results
print("\n---Expense summary---")
print("Rent:",rent)
print("Food:",food)
print("Electricity:",electricity_total)
print("Total Expenese:",total_expense)
print("Each person has to pay:",per_person)






