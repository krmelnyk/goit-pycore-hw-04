from pathlib import Path
from typing import Tuple


def total_salary(path: str) -> Tuple[int, float]:
    """Return the total and average salary values from a CSV-like text file."""
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, raw_line in enumerate(file, start=1):
                line = raw_line.strip()
                if not line:
                    continue

                parts = [part.strip() for part in line.split(",", maxsplit=1)]
                if len(parts) != 2:
                    raise ValueError(
                        f"Пошкоджені дані у файлі {path}: рядок {line_number} має некоректний формат."
                    )

                _, salary_raw = parts
                try:
                    salary = int(salary_raw)
                except ValueError as error:
                    raise ValueError(
                        f"Пошкоджені дані у файлі {path}: рядок {line_number} містить нечислову зарплату."
                    ) from error

                total += salary
                count += 1
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Файл не знайдено: {path}") from error
    except OSError as error:
        raise OSError(f"Не вдалося прочитати файл: {path}") from error

    if count == 0:
        return 0, 0.0

    return total, total / count

if __name__ == "__main__":
    data_file = Path(__file__).resolve().parent.parent / "test_data" / "salary.txt"
    try:
        total, average = total_salary(data_file)
        print(f"Загальна сума заробітної плати: {total},  Середня заробітна плата: {average}")
    except (FileNotFoundError, OSError, ValueError) as error:
        print(f"Помилка: {error}")
