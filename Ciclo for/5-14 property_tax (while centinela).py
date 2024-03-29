#Efrain Robles Pulido

# This program displays property taxes.
 
# TAX_FACTOR is used as a global constant
# for the tax factor.
TAX_FACTOR = 0.0065
# Get the first lot number.
print('Enter the property lot number')
print('or enter 0 to end.')
lot = int(input('Lot number: '))

def show_tax():
    # Get the property value.
    value = float(input('Enter the property value: '))

    # Calculate the property's tax.
    tax = value * TAX_FACTOR

    # Display the tax.
    print('Property tax: $', format(tax, ',.2f'), sep='')

# Continue processing as long as the user
# does not enter lot number 0.

while lot != 0:
# Show the tax for the property.
    show_tax()

# Get the next lot number.
    print('Enter the next lot number or')
    print('enter 0 to end.')
    lot = int(input('Lot number: '))

# The show_tax function gets a property's
# value and displays its tax.

