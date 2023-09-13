# if "kiwi is in fruits, then print value, if not print 0
"""
fruits = {"apple": 3, "pear": 12, "orange": 5}
if_there = fruits.get("kiwi", 0)
print(if_there)

# Same as above, but more verbose
for fruit in fruits:
    if "kiwi" in fruits:
        print(fruits["kiwi"])
    else:
        print(fruit, fruits[fruit])

"""
# Counting the words in a line, making it into a dictionary where the words are the keys and the number of times
# they show up in the list, is the value, find the word that shows up the most.
"""        
text = input("Enter file: ")
file = open(text)

counter = dict()
for line in file:
    # for each word in line, break the line into the words delimited by space
    words = line.split()
    # For each word in the list of words, make a key in counter with the name of the key being the word
    # and if the word is not in the counter, then add it, and increase its value to 1
    for word in words:
        counter[word] = counter.get(word, 0) + 1
        
        
large_word = None
large_count = None

# for the key and the value in the counter dictionary as iterating through the keys and their respective values
for word, count in counter.items():
    # if large word value equals none, or if the of each word in the counter dictionary value is 
    # larger than what is stored as the larger word
    if large_word is None or count > large_word:
        # large_word then equals the value of the just looked at key in the counter dictionary and its respective value
        large_word = word
        large_count = count
"""

text = input("Enter file:")
file = open("../Resources/" + text)
senders = dict()
for line in file:
    if line.startswith("From "):
        line = line.split()
        senders[line[1]] = senders.get(line[1], 0) + 1


most_sent = None
most_sent_count = None

for sender, sender_count in senders.items():
    if most_sent is None or sender_count > most_sent_count:
        most_sent = sender
        most_sent_count = sender_count


print(f"{most_sent} {most_sent_count}")
