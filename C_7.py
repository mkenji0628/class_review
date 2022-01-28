class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        # return self.first_name + " " + self.family_name
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if 0 <= self.age <= 3:
            return 0

        elif 3 < self.age < 20:
            return 1000

        elif 20 <= self.age < 65:
            return 1500

        elif 65 <= self.age < 75:
            return 1200

        else:
            return 500

    def info_csv(self):
        return f"{self.full_name()}, {self.age}, {self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す

print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())

# print(ken.first_name)
# print(ken.family_name)
# print(ken.full_name())
# print(ken.age)
# print(ken.entry_fee())
#
# print(tom.first_name)
# print(tom.family_name)
# print(tom.full_name())
# print(tom.age)
# print(tom.entry_fee())
#
# print(ieyasu.first_name)
# print(ieyasu.family_name)
# print(ieyasu.full_name())
# print(ieyasu.age)
# print(ieyasu.entry_fee())
