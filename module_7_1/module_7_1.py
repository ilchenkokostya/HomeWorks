class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, file_name: str = 'products.txt'):
        self.__file_name = file_name

    def get_products(self, vid=None):
        with open(self.__file_name, 'r') as file:
            products = []
            for line in file:
                name, weight, category = line.split(',')
                products += [[name, float(weight), category[:-1:].strip()]]
            if vid == 'list':
                return products
            else:
                return '\n'.join(str(el).strip('[').strip(']').replace("'", '') for el in products)

    def add(self, *products):
        with open(self.__file_name, 'a') as file:
            for product in products:
                if [product.name, product.weight, product.category] not in self.get_products('list'):
                    file.write(f'{product.name}, {product.weight}, {product.category}\n')
                else:
                    print(f'Продукт {product.name} уже есть в магазине')


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
