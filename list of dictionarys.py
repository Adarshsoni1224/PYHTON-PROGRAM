Student = [
    {"Name": "Rajvi", "Marks": {"English": 83, "Science": 78}},
    {"Name": "Adarsh", "Marks": {"English": 97, "Science": 62}}
]

TOTAL_MARKS = 200
for student in Student:
    name = student["Name"]
    marks = student["Marks"]

    total = marks["English"] + marks["Science"]
    percentage = (total / TOTAL_MARKS) * 100

    print("Name:", name)
    print("Total Marks:", total)
    print("Percentage:", percentage)
    print()