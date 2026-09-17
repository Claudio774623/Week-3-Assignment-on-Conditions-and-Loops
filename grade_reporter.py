# Grade Reporter

scores = [72, 45, 90, 61, 38]

passed = 0
failed = 0
total = 0

for score in scores:

    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print("Score:", score, "Grade:", grade)

    total = total + score

    if score >= 50:
        passed = passed + 1
    else:
        failed = failed + 1

average = total / len(scores)

print("Number passed:", passed)
print("Number failed:", failed)
print("Average:", round(average, 1))

Score: 72 Grade: B
Score: 45 Grade: F
Score: 90 Grade: A
Score: 61 Grade: C
Score: 38 Grade: F
Number passed: 3
Average: 61.2
python grade_reporter.py




Score: 72 Grade: B
Score: 45 Grade: F
Score: 90 Grade: A
Score: 61 Grade: C
Score: 38 Grade: F
Number passed: 3
Number failed: 2
Average: 61.2