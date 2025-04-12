def greet(name):
    print(f'hello ,{name}')

greet('Azahar hossen novel'+'83')

#expense project
expenses=[]
def add_expenses(discription,amount):
    expenses.append({'discription':discription ,'amount':amount})
def view_expenses():
    for expense in expenses:
     print(f'{expense['discription']} :${expense['amount']}')
def calculate_total():
   total=sum(expense['amount'] for expense in expenses)
   print(f'total expences:${total}')

add_expenses('lunch',250)
add_expenses('dinner',250.24)
view_expenses()
calculate_total()