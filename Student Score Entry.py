#Student Score Entry

try:
    exam_score = int(input("Enter examination score: "))
    if exam_score <= 0 or exam_score <= 100:
        print("Valid score.")

except ValueError:
    print("Invalid input. Please enter a number.")

