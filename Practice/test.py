names = [('Sophia', 'Smith'), ('Liam', 'Kim'), ('Olivia', 'Garcia'), ('Noah', 'Muller')]
jobs = [("Teacher", "Da Vinci PS"), ("Student", "Dunbarton High"), ("Nurse", "Rouge Health"), ("Zoo keeper", "Toronto Zoo")]


people = {}
for i in range(len(names)):
    person = {"first_name": names[i][0], "last_name": names[i][1], "job": jobs[i][1], "work_location": jobs[i][1]}
    people[i] = person

print(people)
