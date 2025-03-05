# Input marks for each subject
java = float(input("Enter marks for Java: "))
python = float(input("Enter marks for Python: "))
javascript = float(input("Enter marks for JavaScript: "))
reactjs = float(input("Enter marks for React-js: "))
nodejs = float(input("Enter marks for Node-js: "))

# Calculate total marks
total = 0

if java >= 0:
    total += java
else:
    print("Invalid marks for Java.")

if python >= 0:
    total += python
else:
    print("Invalid marks for Python.")

if javascript >= 0:
    total += javascript
else:
    print("Invalid marks for JavaScript.")

if reactjs >= 0:
    total += reactjs
else:
    print("Invalid marks for React-js.")

if nodejs >= 0:
    total += nodejs
else:
    print("Invalid marks for Node-js.")

# Calculate average marks
average = total / 5

# Display the marksheet
print("Marksheet:")
print(f"Java: {java}")
print(f"Python: {python}")
print(f"JavaScript: {javascript}")
print(f"React-js: {reactjs}")
print(f"Node-js: {nodejs}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average} %")
