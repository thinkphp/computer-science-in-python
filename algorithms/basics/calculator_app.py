def add(a,b):
    return a + b
def sub(a, b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    return a / b

def check_if_the_user_has_finished():
    user_input_accepted = False
    ok_to_finish = True
    while not user_input_accepted:
          user_input = input("Do you want to finish? (y/n): ")
          if user_input == 'y':
             user_input_accepted = True
             ok_to_finish = True
          elif user_input == 'n':
             user_input_accepted = True
             ok_to_finish = False
          else:
             print("Response must be (y/n). Please try again!")
    return ok_to_finish

def operation_choice():
    input_ok = False
    while not input_ok:
        print("Menu options are:")
        print("\t1: Add")
        print("\t2: Substract")
        print("\t3: Multiply")
        print("\t4: Divide")
        print("-----------------")
        user_selection = input("Please make a selection:")
        if user_selection in ('1','2','3','4'):
           input_ok = True
        else:
           print("Invalid input (must be 1 - 4) ")
    return user_selection
def get_numbers_from_user():
    n1 = int(input("a = "))
    n2 = int(input("b = "))
    return n1,n2
def main():
   print("App Calculator")
   finished = False
   while not finished:
    result = 0
    menu_choice = operation_choice()
    a, b = get_numbers_from_user()
    if menu_choice == '1':
       result = add(a,b)
    elif menu_choice == '2':
       result = sub(a,b)
    elif menu_choice == '3':
       result = mult(a,b)
    elif menu_choice == '4':
       result = div(a,b)
    print("Result:", result)
    finished = check_if_the_user_has_finished()
   print("Bye")
main()
