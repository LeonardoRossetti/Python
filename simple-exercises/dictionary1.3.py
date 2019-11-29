people_ages = {
    'John': 38,
    'Mark': 45,
    'Marie': 51
}

age = people_ages.get('John', 'Unknown')
print(age)
age = people_ages.get('Karl', 'Unknown')
print(age)
