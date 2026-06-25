
from ast import Return


global_summary = {}
current_data = []
current_2d_data = []
current_mode = "1D"


def print_doc(name: str, func):
    """Print a function's documentation string for menu help."""
    print(f"\n{name}: {func.__doc__}\n")


def input_1d_data():
    """Read a 1D list of numbers from the user or use sample data."""
    global current_data, current_mode, global_summary
    current_mode = "1D"
    raw = input("Enter numbers separated by spaces (or press enter for sample): ").strip()
    if not raw:
        current_data = [34, 12, 56, 78, 43, 21, 90]
        print("Using sample 1D data:", current_data)
    else:
        current_data = [float(x) if "." in x else int(x) for x in raw.split() if x.strip()]
    global_summary = summarize_dataset(current_data)
    print("Data stored successfully.")


def input_2d_data():
    """Read a 2D list of numbers from the user or use sample 2D data."""
    global current_2d_data, current_mode, global_summary
    current_mode = "2D"
    rows = input("Enter number of rows for 2D data (or press enter for sample): ").strip()
    if not rows:
        current_2d_data = [
            [12, 45, 78],
            [33, 66, 21],
            [90, 10, 34],
        ]
        print("Using sample 2D data:")
        print_2d_list(current_2d_data)
    else:
        n = int(rows)
        current_2d_data = []
        for i in range(n):
            row = input(f"Enter values for row {i + 1} separated by spaces: ").strip()
            current_2d_data.append([float(x) if "." in x else int(x) for x in row.split() if x.strip()])
    all_values = [item for row in current_2d_data for item in row]
    global_summary = summarize_dataset(all_values)
    print("2D data stored successfully.")


def input_data():
    """Allow the user to choose between 1D and 2D data input."""
    choice = input("Choose data type: 1 for 1D, 2 for 2D: ").strip()
    if choice == "2":
        input_2d_data()
    else:
        input_1d_data()


def summarize_dataset(data):
    """Summarize a numeric dataset using built-in functions."""
    if not data:
        return {}
    length = len(data)
    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = total / length
    return {
        "count": length,
        "min": minimum,
        "max": maximum,
        "sum": total,
        "avg": average,
    }


def display_summary():
    """Display summary statistics for the current dataset."""
    if current_mode == "2D":
        data = [item for row in current_2d_data for item in row]
    else:
        data = current_data

    if not data:
        print("No data available. Please input data first.")
        return

    summary = summarize_dataset(data)
    print("\nData Summary:")
    print(f"- Total elements: {summary['count']}")
    print(f"- Minimum value: {summary['min']}")
    print(f"- Maximum value: {summary['max']}")
    print(f"- Sum of values: {summary['sum']}")
    print(f"- Average value: {summary['avg']:.2f}")


def find_duplicates(data):
    """Return a list of duplicate values in the dataset."""
    seen = set()
    duplicates = []
    for item in data:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates


def display_duplicates():
    """Display duplicate values for the current 1D dataset."""
    if not current_data:
        print("No 1D data available. Please input 1D data first.")
        return
    duplicates = find_duplicates(current_data)
    print("\nDuplicate values:" if duplicates else "\nNo duplicate values found.")
    if duplicates:
        print(", ".join(str(x) for x in duplicates))


def display_unique_values():
    """Display unique values from the current dataset."""
    data = current_data if current_mode == "1D" else [item for row in current_2d_data for item in row]
    if not data:
        print("No data available.")
        return
    unique = sorted(set(data), key=data.index if isinstance(data, list) else None)
    print("\nUnique values:")
    print(", ".join(str(x) for x in unique))


def show_args(*args):
    """Accept multiple values using *args and display them."""
    print("\n*args received:")
    for index, value in enumerate(args, start=1):
        print(f"  {index}. {value}")


def show_kwargs(**kwargs):
    """Accept key-value pairs using **kwargs and display a dataset summary."""
    print("\n**kwargs summary:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


def factorial(n):
    """Calculate factorial of n using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative indexes.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def filter_by_threshold(threshold, keep_above=True):
    """Filter current 1D data using a lambda function and threshold."""
    if not current_data:
        print("No 1D data available. Please input 1D data first.")
        return []
    predicate = (lambda x: x >= threshold) if keep_above else (lambda x: x <= threshold)
    result = list(filter(predicate, current_data))
    return result


def sort_1d_data(reverse=False):
    """Sort the current 1D data in place."""
    if not current_data:
        print("No 1D data available. Please input 1D data first.")
        return
    current_data.sort(reverse=reverse)
    order = "descending" if reverse else "ascending"
    print(f"\nSorted data in {order} order:")
    print(", ".join(str(x) for x in current_data))


def sorted_2d_rows(reverse=False):
    """Return a new 2D sorted version of the current 2D dataset."""
    if not current_2d_data:
        print("No 2D data available. Please input 2D data first.")
        return []
    sorted_data = [sorted(row, reverse=reverse) for row in current_2d_data]
    return sorted_data


def display_2d_list(data):
    """Display a 2D list in grid format."""
    if not data:
        print("No 2D data to display.")
        return
    print("\n2D Data Grid:")
    for row in data:
        print(" | ".join(str(x) for x in row))


def statistics_multiple_values():
    """Return multiple statistics values for the current dataset."""
    if current_mode == "2D":
        data = [item for row in current_2d_data for item in row]
    else:
        data = current_data
    if not data:
        print("No data available. Please input data first.")
        return None, None, None, None
    summary = summarize_dataset(data)
    return summary["min"], summary["max"], summary["sum"], summary["avg"]


def display_dataset_stats():
    """Display minimum, maximum, sum, and average as separate values."""
    minimum, maximum, total, avg = statistics_multiple_values()
    if minimum is None:
        return
    print("\nDataset Statistics:")
    print(f"- Minimum value: {minimum}")
    print(f"- Maximum value: {maximum}")
    print(f"- Sum of all values: {total}")
    print(f"- Average value: {avg:.2f}")


def process_sample_args():
    """Demonstrate *args handling by passing sample values."""
    show_args("apple", "banana", "cherry")


def process_sample_kwargs():
    """Demonstrate **kwargs handling with dataset details."""
    show_kwargs(count=len(current_data), mode=current_mode, summary=global_summary)


def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\nWelcome to the Data Analyzer and Transformer Program")
        print("Main Menu:")
        print("1. Input Data")
        print("2. Display Data Summary")
        print("3. Calculate Factorial")
        print("4. Filter Data by Threshold")
        print("5. Sort Data")
        print("6. Display Dataset Statistics")
        print("7. Exit Program")

        choice = input("Please enter your choice: ").strip()

        if choice == "1":
            print_doc("Input Data", input_data)
            input_data()
        elif choice == "2":
            print_doc("Display Data Summary", display_summary)
            display_summary()
        elif choice == "3":
            print_doc("Calculate Factorial", factorial)
            value = int(input("Enter a non-negative integer for factorial: "))
            print(f"Factorial of {value} is: {factorial(value)}")
        elif choice == "4":
            print_doc("Filter Data by Threshold", filter_by_threshold)
            threshold = float(input("Enter a threshold value: "))
            above = input("Keep values above or below threshold? (above/below): ").strip().lower() != "below"
            filtered = filter_by_threshold(threshold, keep_above=above)
            print("Filtered data:", filtered)
        elif choice == "5":
            print_doc("Sort Data", sort_1d_data)
            if current_mode == "2D":
                direction = input("Enter 1 for ascending row sort, 2 for descending row sort: ").strip()
                sorted_rows = sorted_2d_rows(reverse=(direction == "2"))
                if sorted_rows:
                    display_2d_list(sorted_rows)
            else:
                direction = input("Enter 1 for ascending, 2 for descending: ").strip()
                sort_1d_data(reverse=(direction == "2"))
        elif choice == "6":
            print_doc("Display Dataset Statistics", display_dataset_stats)
            display_dataset_stats()
        elif choice == "7":
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number from the menu.")


if __name__ == "__main__":
    main_menu()
