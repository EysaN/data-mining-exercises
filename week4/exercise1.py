"""
Let's build a simple command-line notebook application. Task specification:
Notes are short memos stored in a notebook. Each note should record the day it was written and can
have tags added for easy querying. It should be possible to modify notes. We also need to be able to
search for notes.
"""
from datetime import datetime


class Note:
    """
    This is a Note class which made for data mining class as in intro into Python
    It offer basics funtions to add, delete or print notes
    """
    last_id = 0
    notes_dict = dict()

    def __init__(self, name, body):
        self.name = name
        self.body = body
        self.date = None

    def save(self):
        Note.last_id += 1
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Note.notes_dict[Note.last_id] = self

    @staticmethod
    def delete(_id):
        Note.notes_dict.pop(_id)

    @staticmethod
    def print_note(_id):
        note = Note.notes_dict[_id]
        print("note id", _id, "\nnote name:", note.name, "\nnote date:", note.date, "\nnote body:", note.body)

    @staticmethod
    def print_all_notes():
        for k, v in Note.notes_dict.items():
            print("note id", k, "\nnote name:", v.name, "\nnote date:", v.date)


def run(action, *args):
    if action == "add":
        note_name = input("enter note name: ")
        note_body = input("write your note: ")
        note = Note(note_name, note_body)
        note.save()
    if action == "printall":
        Note.print_all_notes()
    if action == "search":
        note_id = int(input("enter note id:"))
        print(Note.print_note(note_id))
    if action == "delete":
        note_id = int(input("enter note id:"))
        print("note with id %s is deleted" % note_id)


if __name__ == '__main__':
    while 1:
        print('available actions are: "add", "printall", "search", "delete", "close"')
        _action = input("type one: ")
        if _action not in ["add", "printall", "search", "delete", "close"]:
            print("action is not valid")
        elif _action == "close":
            break
        else:
            run(_action)
        print('=' * 15)
