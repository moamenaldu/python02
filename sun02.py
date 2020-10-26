name = input("Add Your Name: ")
age = input("Add Your age: ")
phone = input("Add Your phone: ")
address = input("Add Your address: ")

thisdict = {
    "name": "BBB",
    "age": "25",
    "phone": "0790222",
    "address": "Amman"
    }


thisdict["name"] = name
thisdict["age"] = age
thisdict["phone"] = phone
thisdict["address"] = address



def age_valdation(age):
    if int(age) >= 18:
        print("welcome in Python class")
    else:
        print("sorry")
    return age

age_valdation(thisdict["age"])







# data = {
#     1: 'Admin',
#     2: 'Editor',
#     3: 'Reader'
# }
# print(data)
# print(data[1])