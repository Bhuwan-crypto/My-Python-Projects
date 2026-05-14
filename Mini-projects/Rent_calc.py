#input
#total rent charge of flat
#total electricity unit of 1 month
#unit_per_charge
#Wi-Fi charge
#gas and food charge
#month

#output
# total rent per person
import datetime
date_of_last_rent = input("Enter the date of the last time you paid rent (YY-MM-DD)= ")
try:
    rent_date = datetime.datetime.strptime(date_of_last_rent, "%Y-%m-%d").date() #strptime = “string parse time.”
                                                                                       # It converts a string into a datetime object.
                                                                                       #.date() for only date part no time
except ValueError:
    print("Invalid formate!")
    exit()
    #input
today_date = datetime.date.today()
Total_Rent = int(input("Enter total rent of flat = "))
Electricity_Unit = int(input("Enter total electricity unit  = "))
unit_per_charge_of_electricity = 12
wi_fi_charge = int(input("Enter total wi_fi charge  = "))
gas_food = int(input("Enter total gas and food charge = "))
people = int(input("Enter number of people living in flat ="))

#calculation
total_electricity_bill = Electricity_Unit * unit_per_charge_of_electricity

rent_per_person = (Total_Rent + total_electricity_bill + wi_fi_charge +gas_food)/ people
rent_per_person_per_day =((Total_Rent + total_electricity_bill + wi_fi_charge +gas_food)/ people)/30
final_rent_time = (today_date - rent_date).days
final_rent_per_person =final_rent_time *rent_per_person_per_day
print(f"The total rent per person is {final_rent_per_person}")

