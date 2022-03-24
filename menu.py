"""my lab"""
import sys
from notebook import Notebook, Note

class Menu:
    """
    Display a menu and respond to choices when run.
    """
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
            }

    def display_menu(self):
        """
        function print display menu
        """
        print("""
    Notebook Menu
    1. Show all Notes
    2. Search Notes
    3. Add Note
    4. Modify Note
    5. Quit
    """)

    def run(self):
        """
        Display the menu and respond to choices.
        """
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    def show_notes(self, notes=None):
        """
        fuction to show notes
        """
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
                note.my_id, note.tags, note.memo))

    def search_notes(self):
        """
        function to search notes(
        """
        filterr = input("Search for: ")
        notes = self.notebook.search(filterr)
        self.show_notes(notes)

    def add_note(self):
        """
        function to add note
        """
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        """
        function to modify note
        """
        idd = int(input("Enter a note id: ")) #інт
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(idd, memo)
        if tags:
            self.notebook.modify_tags(idd, tags)

    def quit(self):
        """
        function to quit
        """
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    print(type(Notebook))
    print(type(Note))
    print(dir(Notebook))
    print(dir(Note))
    print(dir(Menu))
    Menu().run()
