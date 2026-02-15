from pathlib import Path


def get_cats_info(path):
    """Parse a cats data file and return a list of dictionaries for each cat."""
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, raw_line in enumerate(file, start=1):
                line = raw_line.strip()
                if not line:
                    continue

                parts = [part.strip() for part in line.split(",")]
                if len(parts) != 3:
                    raise ValueError(
                        f"Пошкоджені дані у файлі {path}: рядок {line_number} має некоректний формат."
                    )

                cat_id, name, age = parts
                if not cat_id or not name or not age:
                    raise ValueError(
                        f"Пошкоджені дані у файлі {path}: рядок {line_number} містить порожні поля."
                    )

                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Файл не знайдено: {path}") from error
    except OSError as error:
        raise OSError(f"Не вдалося прочитати файл: {path}") from error

    return cats

if __name__ == "__main__":
    data_file = Path(__file__).resolve().parent.parent / "test_data" / "cats.txt"
    try:
        cats_info = get_cats_info(data_file)
        for cat in cats_info:
            print(f"id: {cat['id']}, name: {cat['name']}, age: {cat['age']}")
    except (FileNotFoundError, OSError, ValueError) as error:
        print(f"Помилка: {error}")
