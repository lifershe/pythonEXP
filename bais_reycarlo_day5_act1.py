names = ['John', 'Ana', 'Frank']
math = [80, 75, 91]
eng = [83, 76, 89]
sci = [81, 78, 92]
t = 0

ave = []
for m, e, s in zip(math, eng, sci):
    ave.append((m + e + s)/3)

def gradeList(n, m, e, s):

    print(f"{n[t]}'s grade (Math = {m[t]}, English = {e[t]}, Science = {s[t]}) and the average is {round(ave[t], 2)}")

while t <= 2:
    gradeList(names,math,eng,sci)
    t += 1
    continue
