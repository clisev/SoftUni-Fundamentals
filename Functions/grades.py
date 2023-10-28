def grades():
    grade = float(input())
    if grade <= 2 or grade <= 2.99:
        print("Fail")
    elif grade <= 3.49:
        print("Poor")
    elif grade <= 4.49:
        print("Good")
    elif grade <= 5.49:
        print("Very Good")
    elif grade <= 6:
        print("Excellent")


grades()
