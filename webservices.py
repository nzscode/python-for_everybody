import json
data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 256 2598"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

tree = json.loads(data)
print('Name:', tree['name'])
print('Hide:', tree['email']['hide'])

json_data = '[ "Glenn", "Sally", "Jen" ]'
parsed_data = json.loads(json_data)
print(parsed_data)

dat = '''
{
        "users": [
            {
                "status": {
                    "text": "@jazzychad I just bought one .__."
                 },
                 "location": "San Francisco, California",
                 "screen_name": "leahculver",
                 "name": "Leah Culver"
            }
        ]
}
'''

x = json.loads(dat)
print(x['users'][0]['name'])