list1 = [int(n) for n in raw_input("Enter: ").split(",")]
print(list1)
print ("List1 is ") + str(len(list1)) + (" characters long")

list2 = [int(n) for n in raw_input("Enter: ").split(",")]
print(list2)
print ("List2 is ") + str(len(list2)) + (" characters long")

def fizzbuzz(a, b):
    totallength = int(len(list1)) + int(len(list2))
 
    if totallength%3 == 0:
        print("Fizz")
    elif totallength%5 == 0:
        print("Buzz")
    elif totallength%5 == 0 and totallength%3 == 0:
        print(Fizzbuzz)
    else:
        print(totallength)

fizzbuzz(list1,list1)