class Resistor:
    def __init__(self, type_res: str, nominal: int, capacity: int, precision: int):
        self.type_res = type_res
        self.nominal = nominal
        self.capacity = capacity
        self.precision = precision

    def __str__(self):
        return f'Type: {self.type_res}, nominal: {self.nominal}' \
               f' Om, capacity: {self.capacity} Wt, precision: {self.precision} %'

    def __hash__(self):
        sum_n = 0
        for i in range(1, 5):
            sum_n += self.type_res.__hash__() + self.nominal + self.capacity + self.precision
        return sum_n