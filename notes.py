class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, text):
        """Добавить новую заметку"""
        self.notes.append({"id": len(self.notes) + 1, "text": text, "done": False})
        print(f"Заметка добавлена: {text}")

    def show_notes(self):
        """Показать все заметки"""
        if not self.notes:
            print("Заметок пока нет")
            return

        print("\n=== ВСЕ ЗАМЕТКИ ===")
        for note in self.notes:
            status = "✓" if note["done"] else "○"
            print(f"{note['id']}. {status} {note['text']}")
        print("==================\n")

    def complete_note(self, note_id):
        """Отметить заметку как выполненную"""
        for note in self.notes:
            if note["id"] == note_id:
                note["done"] = True
                print(f"Заметка '{note['text']}' отмечена как выполненная")
                return
        print(f"Заметка с id {note_id} не найдена")


def main():
    manager = NoteManager()

    while True:
        print("\n1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Отметить заметку как выполненную")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            text = input("Введите текст заметки: ")
            manager.add_note(text)
        elif choice == "2":
            manager.show_notes()
        elif choice == "3":
            try:
                note_id = int(input("Введите ID заметки: "))
                manager.complete_note(note_id)
            except ValueError:
                print("Введите корректный номер")
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова")


if __name__ == "__main__":
    main()