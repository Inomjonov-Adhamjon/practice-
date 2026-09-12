''' Dunders
      Pythonda dunderlar __ bilan boshlanib __ bilan yakunlanadigan 
      maxsus built-in methodlar va attributelardir
      __builtins__, __init__
'''

messege = "Python: everything is an object"
print(messege)
result = type(messege)
print(result)


'''
built-in tools:
 (1) types = int, str, float, list, dict
 (2) functions = print(), len(), input()
 (3) constants = boolean, none 
'''

print(dir(__builtins__))
