from SalaryDeductions import salDec
from GrossSalary import gross
from NetSalary import  netSal
name = input("Enter name: ")
n1 = float(input("Enter number of hours: "))
sumGross = gross(n1, rph = 500)

l = float(input("Enter Loan: "))
i = float(input("Enter Insurance: "))
t = .12 * sumGross

deducts = salDec(l,i,t)
gs = sumGross
sd = deducts
n = netSal(sd,gs)
print("\nOUTPUT")
print(f"\nName: {name}")
print(f"Hour: {n1}")
print(f"\nGross Salary: {sumGross}")
print(f"\nTax: {t}")
print(f"Loan: {l}")
print(f"Insurance: {i}")
print(f"\nTotal Deductions: {deducts}")
print(f"\nNet Salary: {n}")