name = input("Enter name: ")
math = input("Enter math grade: ")
sci = input("Enter science grade: ")
eng = input("Enter english grade: ")
ave = (float(math) + float(sci) + float(eng)) / 3

math2 = "Math"
sci2 = "Science"
eng2 = "English"

print("Name: " + name.upper())
print("Math Grade: ", float(math))
print("Science Grade: ", float(sci))
print("English Grade: ", float(eng))
print("Average: ", float(ave))

if float(ave) > 100:
	print("\nInvalid range. Please review your inputs.")
elif float(math) > 100:
	print("\nInvalid range. Please review your inputs.")
elif float(sci) > 100:
	print("\nInvalid range. Please review your inputs.")
elif float(eng) > 100:
	print("\nInvalid range. Please review your inputs.")

elif (float(ave) >=75 and float(math) >= 75 and float(sci) >= 75) or \
		(float(ave) >=75 and float(math) >= 75 and float(eng) >= 75) or \
		(float(ave) >=75 and float(sci) >= 75 and float(eng) >= 75):
	print("\nCongratulation! You passed the semester. ")
	if float(math) <= 74:
		print(f"But you need to re-enroll {math2} subject.")
	if float(sci) <= 74:
		print(f"But you need to re-enroll {sci2} subject.")
	if float(eng) <= 74:
		print(f"But you need to re-enroll {eng2} subject.")
elif (float(ave) >=75 and float(math) <= 74 and float(sci) < 74) or \
		(float(ave) >=75 and float(math) < 75 and float(eng) < 75) or \
		(float(ave) >=75 and float(sci) < 75 and float(eng) < 75):
	print("\nSorry, You Failed the semester. Because you didn't passed 2 subject.")

else:
	print("\nSorry, You Failed the semester.")



