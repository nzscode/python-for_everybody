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

# To search through a file
text = open ('../Resources/auguries_of_innocence_william_blake.txt')
for line in text:
    line = line.rstrip()
    print(line)
