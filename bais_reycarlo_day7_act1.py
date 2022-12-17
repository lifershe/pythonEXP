import random
fn = ['Aine', 'Caleigh', 'Rei', 'Caleb', 'Louis', 'Callum', 'Liz', 'Carlo', 'David', 'Aireen']
mn = ['Pangilinan', 'Esguerra', 'Dee', 'Santos', 'de Ocera', 'Smith', 'Jobs', 'James', 'Wade', 'Messi']
ln = ['Lee', 'Ming', 'Oh', 'Park', 'Kim', 'Koh', 'Bais', 'Song', 'Xavier', 'Cruz']
nameBank = []
ans = 1
x = 1

for i in range(10):
    if ans == 1:
        a = random.choice(fn)
        b = random.choice(mn)
        c = random.choice(ln)
        print(f"Congratulations! Your new name is {a} {b} {c}")
        d = a + " " + b + " " + c
        nameBank.append(d)
        x = 1

    elif ans == 2:
        print("\nThank You!")
        break
    while x == 1:
        x = input("Do you want to Random name again (Y/N)? ").lower()

        if x == 'y':
            ans = 1
            continue
        elif x == 'n':
            ans = 2
            break
        elif x != 'y' or x != 'n':
            x = 1
            print("Try again Y or N only")

print(nameBank)