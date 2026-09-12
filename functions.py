''' 
functions: 
  define va call
  parametr va argument
  keyword va default arguments
  scope
'''

print("=====define / call=====")
# python uses indentation

# define


def greet(a):
    print(f"how do u do {a}")


def greeting(b):
    print("return funciton is executed")
    return f"hi {b}"


# call
result1 = greet("adam")
print("result1:", result1)

result2 = greeting("new")
print("result2", result2)


print("=====keyword va default arguments=====")
# define
# call da value berilayotganda undan oldin parametr nomi yozib ketiladi
# shunda qaysi tartibda argument berilishi farqi bolmaydi


def give_greet(name, age):
    print("give_greet is executed")
    return f"hi {name} you are {age} years old"


result3 = give_greet(name="adam", age=21)
print("result3", result3)

# default argument parametrga value berilmasa default value berish


def give_greet2(name, age=21):
    print("give_greet2 is executed")
    return f"hi {name} you are {age} years old"


result4 = give_greet2("adam",)
print("result4", result4)


print("=====Scope in python=====")
b = 100  # 3


def calculate(a, b):  # 2
    c = a * b  # 1
    print(f"c value:", c)


calculate(5, 50)
