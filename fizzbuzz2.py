def get_input():
    
    list1 = [int(n) for n in input("Enter: ").split(",")]
    print(list1)
    print ("List1 is " + str(len(list1)) + " characters long")

    list2 = [int(n) for n in input("Enter: ").split(",")]
    print(list2)
    print ("List2 is " + str(len(list2)) + " characters long")
    print(Fizzbuzz(list1, list2))

def Fizzbuzz(a, b):
    totallength = int(len(a)) + int(len(b))
    if totallength % 3 == 0:
        return 'Fizz'
    elif totallength % 5 == 0:
        return 'Buzz'
    elif totallength % 5 == 0 and totallength % 3 == 0:
        return 'FizzBuzz'
    else:
        return totallength

# get_input()