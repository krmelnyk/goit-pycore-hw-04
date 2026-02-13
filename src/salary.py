from pathlib import Path
from typing import Tuple


def total_salary(path: str) -> Tuple[int, float]:
    """Return the total and average salary values from a CSV-like text file."""
    total = 0
    count = 0

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            _, salary = line.strip().split(",")
            total += int(salary)
            count += 1

    if count == 0:
        return 0, 0.0

    return total, total / count

if __name__ == "__main__":
    data_file = Path(__file__).resolve().parent.parent / "test_data" / "salary.txt"
    total, average = total_salary(data_file)
    print(f"Загальна сума заробітної плати: {total},  Середня заробітна плата: {average}")
