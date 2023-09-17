import json

# JSON Dictionary
data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 123 456 789"
    },
   "email" : {
        "hide" : "yes"
    }
}
'''

info = json.loads(data)
print("Name: ", info["name"])
print("Hide: ", info["email"]["hide"])


# JSON List
input = '''[
    {"id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    {"id" : "009",
    "x" : "7",
    "name" : "Veronica"
    }    
]'''

inf = json.loads(input)
print('User count: ', len(inf))
for item in inf:
    print('Name: ', item['name'])
    print('Id: ', item['id'])
    print('Attribute: ', item['x'])
