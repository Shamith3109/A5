details={"Alic":85,"Ram":100}
a=input("Enter the student's name:")
found = False
for b in details:
    if a == b:
        print(f"{a}'s marks: {details[a]}")
        found = True
        break
if not found:
    print("Student not found.")