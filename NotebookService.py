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