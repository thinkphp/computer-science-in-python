def main():

    try:

       num = int(input("Enter a number"))
       
       result = 19 / num

    except ZeroDivisionError:

       print("Error: cannot divide by zero")

    except ValueError:

       print("Error: invalid input. Please enter a number")
main()
