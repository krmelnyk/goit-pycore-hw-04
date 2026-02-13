from pathlib import Path


def get_cats_info(path):
    """Parse a cats data file and return a list of dictionaries for each cat."""
    cats = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            cat_id, name, age = line.strip().split(",")
            cats.append({
                "id": cat_id,
                "name": name,
                "age": age
            })

    return cats

if __name__ == "__main__":
    data_file = Path(__file__).resolve().parent.parent / "test_data" / "cats.txt"
    cats_info = get_cats_info(data_file)
    for cat in cats_info:
        print(f"id: {cat['id']}, name: {cat['name']}, age: {cat['age']}")
