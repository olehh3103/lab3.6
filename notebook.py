"""My lab"""
import datetime
import doctest

# LAST_ID = 0

class Note:
    """
    Represent a note in the notebook. Match against a
    string in searches and store tags for each note.
    >>> n1 = Note("first")
    >>> n1.my_id
    1
    """
    last_id = 0
    def __init__(self, memo, tags=''):
        """
        initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        # global LAST_ID
        Note.last_id += 1
        self.my_id = Note.last_id

    def match(self, filterr):
        """
        Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.
        """
        return filterr in self.memo or filterr in self.tags


class Notebook:
    """
    Represent a collection of notes that can be tagged,
    modified, and searched.
    >>> n = Notebook()
    >>> n.new_note("hello world")
    >>> n.new_note("hello again")
    >>> len(n.notes)
    2
    >>> n.notes[0].my_id
    2
    >>> n.notes[1].my_id
    3
    >>> n.notes[0].memo
    'hello world'
    >>> len(n.search("hello"))
    2
    >>> len(n.search("world"))
    1
    >>> n.modify_memo(2, "hi world")
    >>> n.notes[0].memo
    'hi world'
    """
    def __init__(self):
        """
        Initialize a notebook with an empty list.
        """
        self.notes = []

    def new_note(self, memo, tags=''):
        """
        Create a new note and add it to the list.
        """
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """
        Locate the note with the given id.
        """
        for note in self.notes:
            if note.my_id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        """
        Find the note with the given id and change its
        memo to the given value.
        """
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        """
        Find the note with the given id and change its
        tags to the given value.
        """
        for note in self.notes:
            if note.my_id == note_id:
                note.tags = tags
                break

    def search(self, filterr):
        """
        Find all notes that match the given filter
        string.
        """
        return [note for note in self.notes if
                note.match(filterr)]

if __name__ == "__main__":
    print(doctest.testmod())
