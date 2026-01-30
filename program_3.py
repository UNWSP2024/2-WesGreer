# Total Purchase Program
# Written by Wesley Greer on 1/30/2026
def calculate_total_purchase():
     # A customer in a store is purchasing five items, ask for the price of each item
  print('I see you have five items to check out!')
item1 = float(input('How much is your first item? '))
item2 = float(input('How much is your second item? '))
item3 = float(input('How much is your third item? '))
item4 = float(input('How much is your fourth item? '))
item5 = float(input('How much is your fifth item? '))
    # display subtotal, sales tax, and the total
subtotal = item1 + item2 + item3 + item4 + item5
sales_tax = subtotal * 0.07
total = subtotal + sales_tax
print(f'The subtotal before tax is ${subtotal:.2f}')
print(f'The sales tax comes out to ${sales_tax:.2f}')
print(f'And the total is ${total:.2f}')

calculate_total_purchase()
