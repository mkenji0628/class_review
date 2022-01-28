class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + " " + self.family_name
        # return f"{self.first_name} {self.family_name}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.full_name()  # "Ken Tanaka" という値を返す
ken.age  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.full_name()  # "Tom Ford" という値を返す
tom.age  # 57 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.age  # 73 という値を返す

print(ken.first_name)
print(ken.family_name)
print(ken.full_name())
print(ken.age)

print(tom.first_name)
print(tom.family_name)
print(tom.full_name())
print(tom.age)

print(ieyasu.first_name)
print(ieyasu.family_name)
print(ieyasu.full_name())
print(ieyasu.age)
