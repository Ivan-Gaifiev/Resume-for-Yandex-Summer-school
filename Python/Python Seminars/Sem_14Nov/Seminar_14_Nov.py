class Cat:

    def __init__(self, name, age, weight, gender, status):
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender
        self.status = status
        self.__damage = 0

    def change_status(self, status):
        if status == "sleep":
            self.status = "sleep"
        else:
            self.status = "awake"
        return self.status

    def str(self):
        return f"Cat {self.name}, {self.age} years old, {self.weight} kg, gender: {self.gender}, status: {self.status}"

    def feed(self):
        self.weight += 0.1
        self.status = "sleep"
        self.__damage -= 10

    @property
    def power(self):
        power = 100
        if self.gender == "female":
            power -= 10
        if self.age < 10:
            power += 10 * self.age
        elif self.age > 10:
            power -= 10 * (self.age - 10)
        if self.weight > 3:
            power -= 20 * self.weight
        power -= self.__damage
        return power

    @property
    def condition(self):
        """
        100-80 perfect
        80-60 good
        60-40 - medium
        40-20 bad
        20-10 weak
        10-0 critical
        """

        if self.__damage >= 80 and self.__damage <= 100:
            return "perfect damage"
        if self.__damage >= 60 and self.__damage < 80:
            return "good damage"
        if self.__damage >= 40 and self.__damage < 60:
            return "medium damage"
        if self.__damage >= 20 and self.__damage < 40:
            return "bad damage"
        if self.__damage >= 10 and self.__damage < 20:
            return "weak damage"
        if self.__damage >= 0 and self.__damage < 10:
            return "critical damage"

    def __gt__(self, other):
        return self.power > other.power

    def hit(self, other):
        if other.status == "sleep":
            other.__damage += 10
        else:
            other.__damage += 5

    def recover(self):
        if self.__damage > 10:
            self.__damage -= 10
        else:
            self.__damage = 0


cat = Cat("Busya", 11, 2, "female", "sleep")
print(cat.__dict__)
cat.change_status("awake")
print(cat.__dict__)
cat
cat.feed()
cat
print(cat.power)
# cat.power = 1000


cat2 = Cat("Marsik", 12, 4, "male", "awake")
print(cat.power)
print(cat > cat2)

print(cat.power)
cat2.hit(cat)
print(cat.power)

cat2.hit(cat)
print(cat.condition)