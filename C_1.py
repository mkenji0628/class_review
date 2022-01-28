class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self):
        return self.first_name + " " + self.family_name
        # return f"{self.first_name} {self.family_name}"


ken = Customer(first_name="Ken", family_name="Tanaka")
ken.full_name()  # "Ken Tanaka" という値を返す

tom = Customer(first_name="Tom", family_name="Ford")
tom.full_name()  # "Tom Ford" という値を返す

print(ken.first_name)
print(ken.family_name)
print(ken.full_name())

print(tom.first_name)
print(tom.family_name)
print(tom.full_name())
