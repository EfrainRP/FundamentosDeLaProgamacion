# Robles Pulido Efrain
#This program calculates sales commission
#Create a variable to control the loop
keep_going= "y"

#Calculate a series of commission

while keep_going == "y": #condicion
    #Get a salesperson's sales and commission rate
    sales=float(input("Enter the amount of sales: "))
    comm_rates=float(input("Enter the commission rate: "))

    #Calculate the commission
    commission= sales * comm_rates

    #Display the commission
    print("The commission is $ ",\
          format(commission, ",.2f"),sep=" ")

    #See if the user wants to do another one
    keep_going= input("Do you want to calculate another " + \
                      "commission (Enter y for yes: ")

