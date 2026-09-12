print("=======Numbers========")
# Pythonda: Veriablelar referencening nomlanishi

# count = 100
# count_type = type(count)

# print(f"The count: {count} The type: {count_type}")

# result1 = count.bit_count()  # method
# result2 = count.numerator    # state
# print(f"method result {result1} state result {result2}")


print("=======strings========")
# Methods: upper(), lower(), title(), find(), replace()

# course = "AI Python engineering"
# result = type(course)
# print(f"Result 1: {result}")

# result = course.title()
# print(f"Result 2: {result}")

# result = course.upper()
# print(f"Result 3: {result}")

# result = course.replace("engineering", "fulllstack")
# print(f"Result 4: {result}")


print("=======Boolean========")
# functions: type(), input(), bool(), int(), str()
# a = input("enter the value of a ...")
# print("value of a is:", a)

# result = a.isnumeric()
# print(f"the input value is numeric {result}")

# Truthy vs Falsy
# Truthy: True 100, -100, "str"
# Falsy: False, 0, "", None
test_falsy = ""
print("Falsy:", bool(test_falsy))

test_truthy = "Mit"
print("Truthy:", bool(test_truthy))
