''' Objects
    1, what is an object
    2, itrable objects and range
    3, dictionary
    4, error handling system
'''
import math
import array  # package / model
from math import ceil, asin

print("====== objects ======")
print(type("hello world"))
print(type(100))
print(type(True))
print(type(math))
print(type(array))


result = math.ceil(97.7)  # call
print("result", result)

result2 = ceil(98.7)
print("result2", result2)


print("====== error handling system ======")

car_dict = dict(name="toyota", year=2025, electric=True)

try:
    print("try ishga tushd")
    # a = car_dict.speed
    result = car_dict["origin"]
    print("result", result)
except KeyError as err:
    print("no property found", err)
except AttributeError as err:
    print("no speed found", err)
# except Exception as err:
#     print("general error:", err)
else:
    print("executed without error")
finally:
    print("closing logic")
