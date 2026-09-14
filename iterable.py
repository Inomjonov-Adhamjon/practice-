print("======== iterable objects ========")
# iterable: takrorlanish hususiyatiga ega bolgan objects
# ex: string, dic, tuple, list, rang, map, filter

text = "MIT"
for letter in text:
    print(f"letter: {letter}")


range_obj = range(9)
print("range", range_obj)
for ele in range_obj:
    print(ele)


print("======== dictionary ========")
# dictionary = json object

person = {"name": "adam", "age": 21, "single": True}
person_obj = dict(name="adam", age=21, single=True)
print(f"person: {person}")
print(f"person_obj: {person_obj}")

# method: get
# name = person_obj["name"]

name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"name: {name}, hobby: {hobby} and balance: {balance}")

del person_obj["single"]
for key in person_obj:
    print(f"key: {key}, value: {person_obj[key]}")
