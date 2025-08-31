import random
from algorithms.sorting import bubble_sort, insertion_sort, quick_sort, selection_sort, merge_sort

def main():
    print("Welcome to Algo Playground!")
    print("Choose a sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Quick Sort")
    print("4. Selection Sort")
    print("5. Merge Sort")

    choice = input("Enter choice (1-5): ")

    # generate random list
    data = [random.randint(1, 100) for _ in range(10)]
    print("Original:", data)

    if choice == "1":
        print("Bubble Sort:", bubble_sort(data.copy()))
    elif choice == "2":
        print("Insertion Sort:", insertion_sort(data.copy()))
    elif choice == "3":
        print("Quick Sort:", quick_sort(data.copy()))
    elif choice == "4":
        print("Selection Sort:", selection_sort(data.copy()))
    elif choice == "5":
        print("Merge Sort:", merge_sort(data.copy()))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
