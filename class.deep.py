print("======== encapsulation ========")
''' Public  private  protected
    name    __name   _protected
'''


class Account():
    # state
    description = "this class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # methods
    def get_balance(self):
        print(f"owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("holder.setter", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
        print("owner name is changed to", new_owner)
        self.__owner = new_owner


my_account = Account("adam", 1000)
my_account.get_balance()

print("---------")
my_account.deposit(1500)
my_account.withdraw(400)
my_account.get_balance()

print("---------")
try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("no target amount state found", err)


print("holder_name before", my_account.holder)

my_account.holder = "john"
print("holder_name after", my_account.holder)
