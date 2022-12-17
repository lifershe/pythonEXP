EmpName = input("Enter employee name: ")
yrsInSrv = input("Enter years-in-service: ")
office = input("Enter office (IT,ACCT or HR only): ")
bonus = 0
choice = str(office.lower())
match choice:
    case "it":
        bonus = 5000
        if int(yrsInSrv) >= 10:
            print("\nHi " + EmpName.upper() + "," + f" your bonus is {bonus*2}.")
        else:
            print("\nHi " + EmpName.upper() + "," + f" your bonus is {bonus}.")
    case "acct":
        bonus = 6000
        if int(yrsInSrv) >= 10:
            print("\nHi " + EmpName.upper() + "," + f" your bonus is {bonus * 2}.")
        else:
            print("\nHi " + EmpName.upper() + "," + f" your bonus is {bonus}.")
    case "hr":
        bonus = 7500
        if int(yrsInSrv) >= 10:
            print("\nHi " + EmpName.upper() + "," + f" your bonus is {bonus * 2}.")
        else:
            print("\nHi " + EmpName.upper() + "," + f" your bonus is {bonus}.")
    case _:
        print("\nInvalid Data. Choose only 'IT','ACCT' and  'HR' only")