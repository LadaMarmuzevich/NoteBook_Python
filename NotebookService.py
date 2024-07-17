import json
import os
from datetime import datetime

NOTES_FILE = 'notes.json'

"""Это функция загружает заметки из файла."""
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            return json.load(file)
    return []

"""Это функция генерирует уникальный идентификатор для заметки."""
def generate_id():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)
            last_id = max([int(note["id"]) for note in notes])
            return str(last_id + 1)
    return "1"

"""Это функция cоздает новую заметку."""
def create_note(title, content):
    note = {
        "id": generate_id(),
        "title": title,
        "content": content,
        "timestamp": datetime.datetime.now().isoformat()
    }
    return note

"""Это функция cохраняет заметки в файл."""
def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

"""Это функция добавляет новую заметку."""
def add_note():
    title = input("Введите заголовок заметки: ")
    content = input("Введите тело заметки: ")
    note = create_note(title, content)
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена.")

"""Это функция читает все заметки."""
def read_notes():
    notes = load_notes()
    if notes:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело: {note['content']}")
            print(f"Дата создания: {note['timestamp']}")
            print("-" * 20)
    else:
        print("Заметок нет.")

"""Это функция читает заметки по дате."""
def read_notes_by_date():
    """Читает заметки по дате."""
    notes = load_notes()
    date_str = input("Введите дату (YYYY-MM-DD): ")
    filtered_notes = [note for note in notes if date_str in note["timestamp"]]
    if filtered_notes:
        for note in filtered_notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело: {note['content']}")
            print(f"Дата создания: {note['timestamp']}")
            print("-" * 20)
    else:
        print("Заметок на эту дату нет.")