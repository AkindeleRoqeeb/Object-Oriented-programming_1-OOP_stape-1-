class item:
    def calculate_total_price(self, x, y):
        return x * y


item1 = item()
item1.name = 'laptop'
item1.location = 'Nigeria'
item1.price = 300
item1.quality = 3
item1.quantity = 200

print(item1.calculate_total_price(item1.price, item1.quality))

item2 = item()
item2.name = 'phone'
item2.price = 300
item2.quality = 634
item2.quantity = 532
item2.location = 'Nigeria'

print(item2.calculate_total_price(item2.price, item2.quality))
