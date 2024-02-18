import time

class Product:
    def __init__(self, ID, Name, Price, Category):
        self.ID = ID
        self.Name = Name
        self.Price = Price
        self.Category = Category

def load_data(file_path):
    products = []
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            product = Product(int(data[0]), data[1], float(data[2]), data[3])
            products.append(product)
    return products

def insert_product(products, new_product):
    products.append(new_product)

def update_product(products, product_id, new_data):
    for product in products:
        if product.ID == product_id:
            product.Name = new_data['Name']
            product.Price = new_data['Price']
            product.Category = new_data['Category']
            break

def delete_product(products, product_id):
    products[:] = [product for product in products if product.ID != product_id]

def search_product(products, key, value):
    result = []
    for product in products:
        if getattr(product, key) == value:
            result.append(product)
    return result

def insertion_sort(products):
    for i in range(1, len(products)):
        key = products[i]
        j = i - 1
        while j >= 0 and key.Price < products[j].Price:
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = key

def display_menu():
    print("\nMenu:")
    print("1. Insert a new product")
    print("2. Update an existing product")
    print("3. Delete a product")
    print("4. Search for a product by ID")
    print("5. Search for a product by Name")
    print("6. Sort and display products by price")
    print("7. Check time on product list")
    print("8. Exit")

def main():
    product_data = load_data('C:/Users/saifs/OneDrive/Desktop/Alg/product_data.txt')

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            new_product = Product(
                int(input("Enter ID: ")),
                input("Enter Name: "),
                float(input("Enter Price: ")),
                input("Enter Category: ")
            )
            insert_product(product_data, new_product)
        elif choice == '2':
            product_id = int(input("Enter the ID of the product to update: "))
            new_data = {
                'Name': input("Enter new Name: "),
                'Price': float(input("Enter new Price: ")),
                'Category': input("Enter new Category: ")
            }
            update_product(product_data, product_id, new_data)
        elif choice == '3':
            product_id = int(input("Enter the ID of the product to delete: "))
            delete_product(product_data, product_id)
        elif choice == '4':
            product_id = int(input("Enter the ID to search for: "))
            result = search_product(product_data, 'ID', product_id)
            print("Search Results:")
            for product in result:
                print(product.ID, product.Name, product.Price, product.Category)
        elif choice == '5':
            product_name = input("Enter the Name to search for: ")
            result = search_product(product_data, 'Name', product_name)
            print("Search Results:")
            for product in result:
                print(product.ID, product.Name, product.Price, product.Category)
        elif choice == '6':
            insertion_sort(product_data)
            print("\nSorted Product Data by Price:")
            for product in product_data:
                print(product.ID, product.Name, product.Price, product.Category)
        elif choice == '7':
            start_time = time.time()
            insertion_sort(product_data)
            end_time = time.time()
            print(f"Time: {end_time - start_time} seconds")
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()


