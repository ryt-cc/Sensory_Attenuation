import csv

# Your data structured as a list of rows
data = [
    ['Name', 'Age', 'Score'],
    ['Alice', 28, 5],
    ['Bob', 34, 10],
    ['Charlie', 22, 100]
]

# Open the file in write mode ('w')
# Always use newline='' to prevent unexpected blank rows
with open('output.csv', mode="a", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write all rows at once
    writer.writerows(data)
    print("Data written to file, thanks for playing")