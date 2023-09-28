# # person = {
# #     "name": "Jane",
# #     "age": 25
# # }
# #
# # print(person.items())
# # print(person.keys())
# # print(person.values())
# # print(len(person))
# #
# #
# # for key, value in person.items():
# #     print(f"key: {key}")
# #     print(f"value: {value}")
# #     print(f"key: {key}, value: {value}")
# #     print("key: ", key)
# #     print("value: ", value)
# #
# #
# # lst = ["hi", "lola", "3", ["rob", "stark"]]
# # print(lst[0])
# # print(len(lst))
# #
# # for i in range(len(lst)):
# #     print(lst[i])
# #
# #
# # for t in range(len(lst[3])):
# #     print(lst[3][t])
# #
# # for i in range(len(lst)):
# #     for t in range(len(lst[i])):
# #         print(f"lst[i][t]: {lst[i][t]}")
# #
# # tup = (11, 72, 'a', 'jasdk')
# # print(tup[0])
# # print(len(tup))
# # print(tup.count())
# # # Open csv
# # import csv
# # import json
# #
# # csv_path = "../Resources/people.csv"
# # csv_data = open(csv_path)
# # csvReader = csv.DictReader(csv_data)
# # csv_dict = {}
# # for rows in csvReader:
# #     print(rows)
# #
# #     #TO convert to a Dictionary:
# #
# #     key = rows['id']
# #     csv_dict[key] = rows
# #
# # print(csv_dict)
#
# # Convert dict to json
# import json
#
# # # Importing dictionary from another module
# # from create_rando_dict import make_dict_rando3_mine
# # rando_dict = make_dict_rando3_mine()
# # rando_json_path = "../Resources/"
# #
# # # To ONLY see the json formatted file.
# # json_obj = json.dumps(rando_dict, indent=4)
# # print(json_obj)
# # # print(rando_dict)
# #
# # # To write to json and save
# # with open(rando_json_path + "json_out.json", 'w') as outfile:
# #     json.dump(rando_dict, outfile)
#
#
# customer = [{
#     "first_name": "Laila",
#     "purchases": [
#         {
#             "item": "Banana",
#             "price": 2.95
#         },
#         {
#             "item": "Pasta",
#             "price": 3.49,
#         }
#     ],
#     "store": "Price Chopper"},
#     {"first_name": "Mindy",
#      "purchases": [
#          {
#              "item": "Carrot",
#              "price": 1.72
#          },
#          {
#              "item": "Olive Oil",
#              "price": 6.58,
#          }
#      ],
#      "store": "Shop Express"}
# ]
#
# #
#
#
# # To write to CSV
# # path = "../Resources/"
# # fields = ["first_name", "purchases", "store"]
# # with open(path + "to_csv.csv", 'w') as file:
# #     writer = csv.DictWriter(file, fieldnames=fields)
# #     # Write Header Row
# #     writer.writeheader()
# #
# #     for row in customer:
# #         writer.writerow(row)
#
# # # TO read from CSV
# # path = "../Resources/"
# # filename = "to_csv.csv"
# # with open(path + filename, 'r') as file:
# #     reader = csv.DictReader(file)
# #
# #     for entry in reader:
# #         print(entry)
#
# # To convert from CSV
#
# # f_names = ["Sophia", "Liam", "Olivia", "Noah", "Emma-Noelle", "Jackson", "Ava", "Lucas", "Isabella", "William", "Ahmed",
# #            "Mei", "Diego", "Fatima", "Jovan", "Amina", "Svetlana", "Priya", "Robert", "Tracy"]
# # l_names = ["Smith", "Kim", "García", "Müller", "Patel", "Nguyen", "Silva", "Yamamoto", "Martinez", "Rossi", "Khan",
# #            "Hernandez", "Andersson", "Li", "Petrov", "Santos", "O'Connor", "Alves", "Gonzalez", "Dubois"]
# # grocery_items = ["Apples", "Bananas", "Milk", "Bread", "Eggs", "Chicken", "Pasta", "Rice", "Cereal", "Tomatoes",
# #                  "Potatoes", "Carrots", "Spinach", "Orange Juice", "Coffee", "Cheese", "Yogurt", "Onions",
# #                  "Canned Soup", "Toilet Paper"]
#


# List to csv
import json
f_names = ["Sophia", "Liam", "Olivia", "Noah"]
l_names = ["Smith", "Kim", "Garcia", "Muller"]

path = "../Resources/"
# full_names = []
# fields = ["First_Name", "Last_Name"]
#
# full_names.append(fields)
#
# for i in range(len(f_names)):
#     full_names.append([f_names[i], l_names[i]])
#
# path = "../Resources/"
# with open(path + "people3.json", 'w') as file:
#     json.dump(full_names, file, sort_keys=False, indent=4)


with open(path + 'demo.html', 'w') as file:
    for i in range(len(f_names)):
        file.writelines("<li>" + f_names[i]+"," + l_names[i] + "</li>" + "\n")

