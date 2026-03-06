marks = int(input("Enter marks: "))
income = int(input("Enter family income: "))

if marks >= 85 and income < 300000:
    print("Scholarship Granted")
else:
    print("Not Eligible")