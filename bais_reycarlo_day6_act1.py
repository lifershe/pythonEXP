dict = {}
ans =1
er =1
while True:

    if ans == 1:
        key = input("Enter Key: ")
        val = input("Enter Value: ")
        dict[key] = val;
        print("\nCurrent data: ", dict)
        er = 1

    elif ans == 2:
        dkey = input("Enter Key to delete: ")
        if dkey in dict:
            del dict[dkey];
            if dict == {}:
                print("No records found! Add another key and value!")
                ans = 1
                continue
        else:
            print("Data doesn't exist!")
            print("Current data: ", dict)
            continue
            er =1

        print("Current data: ", dict)
        er =1
    elif ans == 3:
        print("Thank You!")
        break

    while er == 1:
        b = input("""
    Alert! >>>
    Enter 1 to add more data
    Enter 2 to delete existing data
    Enter 3 to end program           
    Choose your answer: """)
        print("\nCurrent data: ", dict)

        if b == '1':
            er = 0
            continue

        elif b == '2':
            er = 0
            ans = 2

        elif b == '3':
            er = 0
            ans = 3

        elif b != '1' or b!= '2' or b != '3':
            er = 1
            continue
