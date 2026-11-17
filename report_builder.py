import csv

try:
    with open("hubs.csv", "r") as f:
        rows = list(csv.DictReader(f))
except FileNotFoundError:
    rows = []

if len(rows) == 0:
    print("hubs.csv not found")
else:
    total = 0
    passed = 0

    for row in rows:
        score = int(row["score"])
        total += score

        if score >= 50:
            passed += 1

    average = round(total / len(rows), 1)

    with open("report.txt", "w") as f:
        f.write("LEARNER REPORT\n")
        f.write("Total learners: " + str(len(rows)) + "\n")
        f.write("Passed: " + str(passed) + "\n")
        f.write("Failed: " + str(len(rows) - passed) + "\n")
        f.write("Average score: " + str(average) + "\n")

    print("Report written to report.txt")