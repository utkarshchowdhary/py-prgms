## Inheritance


class Clothing:
    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, price):
        self.price = price

    def calculate_discount(self, discount):
        return self.price * (1 - discount)

    def calculate_shipping(self, weight, rate):
        return weight * rate


class Shirt(Clothing):
    def __init__(self, color, size, style, price, long_or_short):

        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short

    def double_price(self):
        self.price = 2 * self.price


class Pants(Clothing):
    def __init__(self, color, size, style, price, waist):

        Clothing.__init__(self, color, size, style, price)
        self.waist = waist

    def calculate_discount(self, discount):
        return self.price * (1 - discount / 2)


class Blouse(Clothing):
    def __init__(self, color, size, style, price, country_of_origin):
        Clothing.__init__(self, color, size, style, price)
        self.country_of_origin = country_of_origin

    def triple_price(self):
        return 3 * self.price


def check_results():
    blouse = Blouse("blue", "M", "luxury", 40, "Brazil")

    print("Shipping:", blouse.calculate_shipping(0.5, 3))
    print("TriplePrice:", blouse.triple_price())


check_results()
