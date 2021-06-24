credit = [21, 21, 23, 23, 17, 26, 22, 20]
gpa = [8, 7.33, 8.22, 8.13, 9.29, 8.23, 9.55, 9.6]

cgpa = sum(c * g for c, g in zip(credit, gpa)) / sum(credit)

print(round(cgpa, 2))
