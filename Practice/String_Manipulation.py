# To open a file:
"""
text = open ('../Resources/auguries_of_innocence_william_blake.txt')
"""


# To open and print the lines of a file
"""
text = open ('../Resources/auguries_of_innocence_william_blake.txt')
for line in text:
    print(line)
    """

# To open and read the whole text
"""
text = open ('../Resources/auguries_of_innocence_william_blake.txt')
whole_text = text.read()
print(whole_text)
"""

# To open and read the whole text as a single line
"""
text = open ('../Resources/auguries_of_innocence_william_blake.txt')
whole_text = text.readlines()
print(whole_text)
"""

# To go through an entire file and remove ending '\n'
"""
text = open ('../Resources/auguries_of_innocence_william_blake.txt')
for line in text:
    line = line.rstrip()
    print(line)
"""

# To Open a file, search something within, split the result, and tally an amount.
"""
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count += 1
        colon_index = line.index(":") + 1
        num = int(line[colon_index:].strip())
        total += num
        continue
    print(line)
average = total / count
print(f"Average spam confidence: {average}")

line = "X-DSPAM-Confidence:    032136223"
index = line.index(":") + 1
line1= line[index:].strip()
print(line1)
"""
