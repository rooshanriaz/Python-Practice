"""favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name)

for language in favorite_languages.values():
    print(language)
"""

"""favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',}"""

"""friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}.")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll.")"""

"""for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")"""

"""print("The following languages have been mentioned:")
for lanugage in favorite_languages.values():
    print(lanugage.title())"""

"""Nested Dictionaries"""

"""alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
"""
"""aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")

print(f"Total number of aliens is:{len(aliens)}")"""
"""aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'fast'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'medium'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")"""

"""pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese']
        }

print(f"You ordered a {pizza['crust']}- crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")"""

"""favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n {name.title()} favorite languages are:")
    for lanugage  in languages:
        print(f"{lanugage}")"""

"""users = {
    'aeinstein' : {
        'first_name' : 'albert',
        'last_name' : 'einstein',
        'location' : 'princeton',
    },
    'mcurie': {
     'first_name' : 'marie',
     'last_name' : 'curie',
     'location' : 'paris',
    },

}

for username, userinfo in users.items():
    print(f"\n Username: {username}")
    full_name = f"{userinfo['first_name']} {userinfo['last_name']}"
    location = userinfo['location']

    print(f"\t Full Name: {full_name.title()}")
    print(f"\t Location: {location.title()}")"""

"""keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

#rest_dict = dict(zip(keys, values))

#print(rest_dict)

res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})

print(res_dict)"""

"""dict1 = {'Ten' : 10, 'Twenty' : 20, 'Thirty' : 30}
dict2 = {'Thirty' : 30, 'Fourty' : 40, 'Sixty' : 60}

merge_dict = {**dict1, **dict2}
print(merge_dict)"""

"""sampleDict = {
    'class': {
        'student': {
            'name': 'Mike',
            'marks': {
                'Physics': 70,
                'History': 80,
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['History'])
"""

"""sampleDict = {
    'name': 'Kelly',
    'age': 25,
    'salary': 8000,
    'city': 'New York'
}

keys = ['name', 'salary']

for k in keys:
   sampleDict.pop(k)

print(sampleDict)"""
"""keys = ['name', 'salary', 'city']

res = dict()

for k in keys:
    res.update({k: sampleDict[k]})
print(res)"""
"""sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sample_dict.values():
    print("200 is present in the dictionary")"""


