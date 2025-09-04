try:
    num = float(input("Enter a number: "))
    print(num * num)
except ValueError:
    print("Please enter a valid number!")
else:
    print("No errors occurred!")