sub1 = int(input("Enter marks  subject 1 : "))
sub2 = int(input("Enter marks  subject 2 : "))
sub3 = int(input("Enter marks  subject 3 : "))
avg = (sub1 + sub2 + sub3) / 3
if avg >= 90:
    print("Grade: A")
elif avg >= 80:
    print("Grade: B")
elif avg >= 70:
    print("Grade: C")
elif avg >= 60:
    print("Grade: D")
else:
    print("Grade: F")