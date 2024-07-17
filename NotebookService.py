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

"""Генерирует уникальный идентификатор для заметки."""
def generate_id():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)
            last_id = max([int(note["id"]) for note in notes])
            return str(last_id + 1)
    return "1"