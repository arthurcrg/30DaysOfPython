# open('filename', mode(can be r, a, w, x, t, b)): Opens a file and returns a file object.
# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# Opening files for reading (the default mode)
f = open('C:\\Coisas\\UFABC\\2026\\Recesso (08 - 09)\\30DaysOfPython\\day_19\\hyrule.txt')
print(f)

# read(): Reads the content of the file. If no size is specified, it reads the entire file.
print(f.read())

print(f.read(5))  # Reads the first 5 characters of the file

print(f.readline())  # Reads the first line of the file

print(f.readlines())  # Reads all the lines of the file and returns them as a list

lines = f.read().splitlines()  # Reads the entire file and splits it into a list of lines
print(lines)

# After opening a file, we should always close it to free up system resources.
f.close()

# It's common to forget to close a file, so we use "with" to close it automatically
with open('C:\\Coisas\\UFABC\\2026\\Recesso (08 - 09)\\30DaysOfPython\\day_19\\hyrule.txt') as f:
    print(f.read())

# Opening files for writing and updating
# "w" - Write - Opens a file for writing, creates the file if it does
with open('C:\\Coisas\\UFABC\\2026\\Recesso (08 - 09)\\30DaysOfPython\\day_19\\hyrule.txt', 'w') as f:
    f.write('At the very edge of this kingdom, there lay a small forest.\n')
    f.write('Within it, an ancient, solitary tree quietly watched over the inhabitants of the forest.\n')

# "a" - Append - Opens a file for appending, creates the file if it does not exist
with open('C:\\Coisas\\UFABC\\2026\\Recesso (08 - 09)\\30DaysOfPython\\day_19\\hyrule.txt', 'a') as f:
    f.write('The tree was a silent witness to the passage of time, its branches swaying gently in the wind.\n')
    f.write('It had seen countless seasons come and go, and it had stood firm through storms and sunshine alike.\n')

# Deleting a file
import os # importing os module
if os.path.exists('C:\\Coisas\\UFABC\\2026\\Recesso (08 - 09)\\30DaysOfPython\\day_19\\hyrule.txt'):
    os.remove('C:\\Coisas\\UFABC\\2026\\Recesso (08 - 09)\\30DaysOfPython\\day_19\\hyrule.txt') # deleting the file
else:
    print('The file does not exist') # avoiding the FileNotFoundError

# File Types

# JSON File: JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is often used for transmitting data in web applications.
pokemon_json = {"name": "Pikachu", "type": "Electric", "level": 5}
import json # importing json module

# Changing JSON to dictionary
pokemon_dict = json.loads(json.dumps(pokemon_json))
print(pokemon_dict) # {'name': 'Pikachu', 'type': 'Electric', 'level': 5}

# Changing dictionary to JSON
pokemon_json = json.dumps(pokemon_dict)
print(pokemon_json) # {"name": "Pikachu", "type": "Electric", "level": 5}

# Saving as JSON file
with open('C:\\Coisas\\UFABC\\2026\\Recesso (08 - 09)\\30DaysOfPython\\day_19\\pokemon.json', 'w') as f:
    json.dump(pokemon_dict, f, ensure_ascii=False, indent=4) # Writing JSON data to a file

# File with CSV (Comma Separated Values) format: CSV is a simple file format used to store tabular data, such as a spreadsheet or database. Each line of the file is a data record, and each record consists of one or more fields, separated by commas.
import csv # importing csv module
with open('C:\\Coisas\\UFABC\\2026\\Recesso (08 - 09)\\30DaysOfPython\\day_19\\pokemon.csv', 'w', newline='') as f:
    csv_reader = csv.reader(f, delimiter=',') # Creating a CSV reader object (we use , as the delimiter)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a {row[1]} type pokemon and is at level {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

# xlsx File: XLSX is a file format used by Microsoft Excel to store spreadsheet data. It is based on the Open XML format and is used for storing data in a tabular form, including text, numbers, formulas, and formatting.
# we will install the module after we cover packages and pip

# xml File: XML (eXtensible Markup Language) is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable. It is used to store and transport data, and it allows users to define their own tags to describe the data.
import xml.etree.ElementTree as ET # importing xml module
tree = ET.parse('C:\\Coisas\\UFABC\\2026\\Recesso (08 - 09)\\30DaysOfPython\\day_19\\pokemon.xml') # parsing the XML file
root = tree.getroot() # getting the root of the XML file
print(root.tag) # printing the root tag
print(root.attrib) # printing the root attributes
for child in root:
    print(child.tag, child.attrib) # printing the child tags and attributes

