def minutes_to_seconds(minutes):
    return minutes * 60

try:
   minutes = int(input("enter minutes "))
   seconds = minutes_to_seconds(minutes)
   print(f"{minutes} minutes is equal to {seconds} seconds.")
except ValueError:
    print("cannot be charcter ")

print("***********************")


def Years_to_Days(years):
    return years * 365

try:
   years = int(input("enter years "))
   days = Years_to_Days(years)
   print(f"{years} years is equal to {days} days.")
except ValueError:
    print("cannot be echarcter ")
print("*********************")


def get_last_item(my_list):
    return my_list[-1]


mylist = input("please inter your list :")
li = mylist.split(",")
print("Last item in homogeneous list:", get_last_item(li))

print("*************************")


def parity_analysis(number):
    mysum = 0
    for c in number:
        mysum += int(c)
    if (int(number)%2) == (mysum%2):
        return True
    else:
        return False


numbers = input("enter your number")
print(parity_analysis(numbers))
