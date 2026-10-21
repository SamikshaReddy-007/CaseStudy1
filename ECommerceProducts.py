
# E-commerce Product Sorting Using Divide and Conquer
# Algorithm: Merge Sort

def display_products(products):
    """Display all products with their prices."""
    print("\n{:<5} {:<25} {:>10}".format("No.", "Product Name", "Price (Rs.)"))
    print("-" * 45)

    for i, product in enumerate(products, start=1):
        print("{:<5} {:<25} {:>10.2f}".format(
            i, product["name"], product["price"]
        ))


def merge_sort(products):
    """Sort products by price using the Merge Sort algorithm."""

    if len(products) <= 1:
        return products

    # Divide the list into two halves
    mid = len(products) // 2
    left_half = merge_sort(products[:mid])
    right_half = merge_sort(products[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """Merge two sorted lists based on product price."""
    sorted_products = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["price"] <= right[j]["price"]:
            sorted_products.append(left[i])
            i += 1
        else:
            sorted_products.append(right[j])
            j += 1

    # Add any remaining products
    sorted_products.extend(left[i:])
    sorted_products.extend(right[j:])

    return sorted_products


def main():
    # Sample e-commerce product inventory
    products = [
        {"name": "Laptop", "price": 55000},
        {"name": "Headphones", "price": 1500},
        {"name": "Smartphone", "price": 25000},
        {"name": "Keyboard", "price": 1200},
        {"name": "Smart Watch", "price": 3500},
        {"name": "Mouse", "price": 800},
        {"name": "Tablet", "price": 18000},
    ]

    while True:
        print("\n===== E-COMMERCE PRODUCT SORTING SYSTEM =====")
        print("1. Display All Products")
        print("2. Sort Products by Price (Low to High)")
        print("3. Sort Products by Price (High to Low)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            display_products(products)

        elif choice == "2":
            sorted_products = merge_sort(products)
            print("\nProducts Sorted by Price (Low to High):")
            display_products(sorted_products)

        elif choice == "3":
            sorted_products = merge_sort(products)
            sorted_products.reverse()
            print("\nProducts Sorted by Price (High to Low):")
            display_products(sorted_products)

        elif choice == "4":
            print("Thank you for using the Product Sorting System!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
