#使用一个字典来存储一个人的信息，包括名、姓、年龄和居住的城市。该字典应包含键 first_name、last_name、age 和 city。将存储在该字典中的每项信息都打印出来。

person = {
    "first_name": "huang",
    "last_name": "yu",
    "age": 18,
    "city": "beijing",
}

print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])
print(person)
print(person.keys())
print(person.values())

print(person.get("first_name"))
print(person.get("last_name"))  
print(person.get("age"))
print(person.get("city"))
print(person.get("second_name"))
