# goit-pycore-hw-04

Набір CLI-завдань з `Python Core`: робота з файлами, рекурсивний обхід директорій та простий консольний асистент.

## Швидкий старт

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск скриптів

| Скрипт | Що робить | Команда |
|---|---|---|
| `src/salary.py` | Рахує загальну та середню зарплату з `test_data/salary.txt` | `python3 src/salary.py` |
| `src/cats.py` | Зчитує дані котів з `test_data/cats.txt` | `python3 src/cats.py` |
| `src/directory_tree.py` | Виводить дерево директорій у кольорі | `python3 src/directory_tree.py path/to/directory` |
| `src/main.py` | Запускає CLI-бота з контактами | `python3 src/main.py` |

## Команди асистента

- `hello`
- `add <name> <phone>`
- `change <name> <phone>`
- `phone <name>`
- `all`
- `exit` або `close`

## Структура проєкту

```text
.
├── README.md
├── requirements.txt
├── src
│   ├── assistant
│   │   ├── __init__.py
│   │   ├── handlers.py
│   │   └── parser.py
│   ├── cats.py
│   ├── directory_tree.py
│   ├── main.py
│   └── salary.py
└── test_data
    ├── cats.txt
    └── salary.txt
```
