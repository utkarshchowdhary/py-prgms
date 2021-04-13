class Pants:
    def __init__(self, color, waist_size, length, price):

        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):

        self.price = new_price

    def discount(self, percentage):

        return self.price * (1 - percentage)


class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary):

        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants_object):

        self.pants_sold.append(pants_object)

    def display_sales(self):

        for pants in self.pants_sold:
            print(
                "color: {}, waist_size: {}, length: {}, price: {}".format(
                    pants.color, pants.waist_size, pants.length, pants.price
                )
            )

    def calculate_sales(self):

        total = 0
        for pants in self.pants_sold:
            total += pants.price

        self.total_sales = total

        return total

    def calculate_commission(self, percentage):

        sales_total = self.calculate_sales()
        return sales_total * percentage


def check_results():
    pants = Pants("red", 35, 36, 15.12)

    pants.change_price(10)
    print("Pants price changed", pants.price)

    print("Pants price After discount", pants.discount(0.1))

    pants_one = Pants("red", 35, 36, 15.12)
    pants_two = Pants("blue", 40, 38, 24.12)
    pants_three = Pants("tan", 28, 30, 8.12)

    salesperson = SalesPerson("Amy", "Gonzalez", 2581923, 40000)

    salesperson.sell_pants(pants_one)
    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)

    print("No of pants sold", len(salesperson.pants_sold))
    print("Total sale", round(salesperson.calculate_sales(), 2))
    print("Commission", round(salesperson.calculate_commission(0.1), 2))


check_results()
