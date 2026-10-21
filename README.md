# E-commerce Product Sorting Using Divide and Conquer

## 1. Project Description

The E-commerce Product Sorting System is a Python-based application that organizes products according to their prices using the Divide and Conquer algorithm. In online shopping platforms, customers often need to compare products based on price to find affordable options quickly. When the number of products increases, sorting them efficiently becomes important.

This project implements the **Merge Sort algorithm**, a popular Divide and Conquer technique. The algorithm divides the list of products into smaller sublists, sorts each sublist recursively, and merges them to produce a sorted list.

The system allows users to display all products, sort products by price in ascending order (low to high), and sort products by price in descending order (high to low). It demonstrates how algorithmic strategies can improve data organization and make product searching and comparison more convenient.

## 2. Objectives

- To understand the Divide and Conquer algorithmic strategy.
- To implement Merge Sort using Python.
- To sort e-commerce products according to their prices.
- To display products in ascending and descending order.
- To analyze the time and space complexity of the algorithm.
- To understand the practical application of sorting algorithms in e-commerce systems.

## 3. Problem Statement

E-commerce platforms contain numerous products with different prices. Displaying products in an unsorted manner makes it difficult for customers to compare prices and identify affordable products. Therefore, an efficient sorting technique is required to arrange products according to their prices.

The objective of this project is to develop a Python application that sorts a list of e-commerce products by price using the Merge Sort algorithm based on the Divide and Conquer strategy.

## 4. Technologies Used

- **Programming Language:** Python
- **IDE:** Visual Studio Code
- **Algorithm:** Merge Sort
- **Algorithmic Strategy:** Divide and Conquer
- **Data Representation:** List of dictionaries

## 5. Features

- Display the complete list of products.
- Sort products by price from low to high.
- Sort products by price from high to low.
- Display product names and prices in a tabular format.
- Provide a menu-driven interface.
- Handle invalid menu choices.
- Demonstrate efficient sorting using Merge Sort.

## 6. Algorithm: Merge Sort

Merge Sort follows the Divide and Conquer approach and works in three main stages.

**Divide:** Split the product list into two halves until each sublist contains one or zero elements.

**Conquer:** Recursively sort each half using the Merge Sort algorithm.

**Combine:** Merge the sorted halves into a single sorted list by comparing product prices.

### Algorithm Steps

1. Start the program.
2. Initialize the product list with product names and prices.
3. Display the main menu.
4. Accept the user's choice.
5. If the user selects display products, show the original list.
6. If ascending sorting is selected, apply Merge Sort and display the sorted products.
7. If descending sorting is selected, sort the products and reverse the resulting order.
8. If the user selects exit, terminate the program.
9. Otherwise, display an invalid-choice message.
10. Repeat until the user exits.

## 7. Divide and Conquer Strategy

Divide and Conquer is an algorithm design technique in which a large problem is divided into smaller subproblems. Each subproblem is solved independently, and the solutions are combined to obtain the final result.

In this project, Merge Sort divides the product list into smaller parts, sorts the parts recursively, and merges them according to product prices.

This approach is efficient for sorting large datasets because it consistently reduces the problem size and combines the results systematically.

## 8. Sample Input

The system contains the following sample products:

| Product Name | Price (₹) |
|---|---:|
| Laptop | 55000 |
| Headphones | 1500 |
| Smartphone | 25000 |
| Keyboard | 1200 |
| Smart Watch | 3500 |
| Mouse | 800 |
| Tablet | 18000 |

## 9. Sample Output

When the user selects option 2, the products are sorted by price in ascending order.

```text
Products Sorted by Price (Low to High):

No.   Product Name              Price (Rs.)
---------------------------------------------
1     Mouse                        800.00
2     Keyboard                    1200.00
3     Headphones                  1500.00
4     Smart Watch                 3500.00
5     Tablet                     18000.00
6     Smartphone                 25000.00
7     Laptop                     55000.00
```

When the user selects option 3, the products are displayed from highest to lowest price.

## 10. Time and Space Complexity Analysis

Merge Sort divides the list into two halves at each level of recursion and merges the sorted results.

**Time Complexity:**

- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

Here, n represents the number of products.

**Auxiliary Space Complexity:** O(n), because additional lists are used during the merging process.

Merge Sort is suitable for efficiently sorting large product lists because its worst-case time complexity is O(n log n).

## 11. Applications

- Sorting products on e-commerce websites.
- Arranging products by price, rating, or popularity with suitable modifications.
- Organizing inventory records.
- Comparing product prices.
- Preparing sorted product catalogues.
- Demonstrating Divide and Conquer in algorithm design.

## 12. Advantages

- Efficient for sorting large datasets.
- Guarantees O(n log n) time complexity.
- Maintains the relative order of equal-price products in this implementation.
- Uses a simple and systematic algorithm.
- Can be adapted to sort products using different attributes.

## 13. Limitations

- Requires additional memory during merging.
- The current version uses a predefined product list.
- Product information is not stored permanently.
- It does not connect to a real e-commerce database or website.
- It sorts products by price only, unless modified.

## 14. Future Scope

- Add options to insert, update, and delete products.
- Store product details in a database or file.
- Add sorting by product name, rating, or category.
- Integrate a search function to find products.
- Develop a graphical user interface.
- Connect the application to a product inventory system.

## 15. Conclusion

The E-commerce Product Sorting System demonstrates the practical implementation of the Divide and Conquer strategy through the Merge Sort algorithm. The application sorts products according to their prices in ascending and descending order and provides a simple menu-driven interface.

The project helps in understanding recursion, list manipulation, algorithm design, and complexity analysis. It also demonstrates how efficient sorting algorithms can be applied to product organization in e-commerce applications.

## 16. References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C. *Introduction to Algorithms*. MIT Press.
2. Python Software Foundation. *Python Documentation*. https://docs.python.org/3/
3. GeeksforGeeks. *Merge Sort Algorithm*. https://www.geeksforgeeks.org/merge-sort/
4. Programiz. *Merge Sort Algorithm*. https://www.programiz.com/dsa/merge-sort
