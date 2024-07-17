from NotebookService import add_note,read_notes,read_notes_by_date,edit_note,delete_note
def main():
    while True:
        command = input("Введите команду (add, read, read_date, edit, delete, exit): ")

        if command == "add":
            add_note()
        elif command == "read":
            read_notes()
        elif command == "read_date":
            read_notes_by_date()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "exit":
            break
        else:
            print("Неверная команда.")

if __name__ == "__main__":
    main()