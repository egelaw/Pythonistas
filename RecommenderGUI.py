# Authors: Ismail Gul and Endalkachew Bogale Gelaw
# Date: 05/XXXXXXX/2024
# Description: This is a GUI program that converts between smoots and meters.

import tkinter
from tkinter import ttk
from Recommender import Recommender


class RecommenderGUI:
    def __init__(self):
        # Creates an instance of a Recommender object and stores it in a variable
        self.__recommender = Recommender()

        # Creates a Toplevel main window, with an appropriate title, and dimensions of 1200
        # pixels wide by 800 pixels tall
        self.__main_window = tkinter.Tk()
        self.__main_window.title("Media Recommender")
        self.__main_window.geometry("1200x800")

        # Contains a notebook tab to display all of the book titles and authors, as well as the book
        # statistics
        self.__book_notebook = ttk.Notebook(self.__main_window)

        # Frame for the buttons
        self.__buttons_frame = tkinter.Frame(self.__main_window)
        self.__buttons_frame.pack(side='bottom')

        # Buttons
        self.__load_shows_button = tkinter.Button(self.__buttons_frame, text='Load Shows', command=self.load_shows)
        self.__load_shows_button.pack(side='left', padx=75)

        self.__load_books_button = tkinter.Button(self.__buttons_frame, text='Load Books', command=self.load_books)
        self.__load_books_button.pack(side='left', padx=75)

        self.__load_associations_button = tkinter.Button(self.__buttons_frame, text='Load Associations',
                                                         command=self.load_associations)
        self.__load_associations_button.pack(side='left', padx=75)

        self.__credit_info_button = tkinter.Button(self.__buttons_frame, text='Credits', command=self.credit_info_box)
        self.__credit_info_button.pack(side='left', padx=75)

        self.quit_button = tkinter.Button(self.__buttons_frame, text='Quit', command=self.__main_window.quit)
        self.quit_button.pack(side='left', padx=75)

        # pack notebook after buttons are packed
        self.__book_notebook.pack(expand=True, fill='both')

        # Books tab
        self.__book_tab = tkinter.Frame(self.__book_notebook)
        self.__book_notebook.add(self.__book_tab, text='Books')

        # Frame for the book_text widget and its scrollbar
        self.__book_frame = tkinter.Frame(self.__book_tab)

        # Frame for the book_stats
        self.__book_stats_frame = tkinter.Frame(self.__book_tab)

        # pack frames
        self.__book_frame.pack(expand=True, fill='both')
        self.__book_stats_frame.pack(expand=True, fill='both')

        # Text widget to display the books
        self.__book_text = tkinter.Text(self.__book_frame, wrap='word')
        # Default text to display
        self.__book_text.insert(tkinter.END, "No books have been loaded yet.")
        self.__book_text.config(state='disabled')

        # a vertical scrollbar
        self.__scrollbar = tkinter.Scrollbar(self.__book_frame, orient='vertical', command=self.__book_text.yview)
        self.__scrollbar.pack(side='right', fill='y')

        self.__book_text.config(yscrollcommand=self.__scrollbar.set)
        self.__book_text.pack(expand=True, fill='both')

        # stats text
        self.__book_stats_text = tkinter.Text(self.__book_stats_frame, wrap='word')
        self.__book_stats_text.pack(expand=True, fill='both')
        self.__book_stats_text.insert(tkinter.END, "No books have been loaded yet.")
        self.__book_stats_text.config(state='disabled')

    def load_shows(self):
        self.__recommender.load_shows()

    def load_associations(self):
        self.__recommender.load_associations()

    def credit_info_box(self):
        pass

    # ========================================================
    # Define the load_books method for the Load Books button
    def load_books(self):
        self.__recommender.load_books()
        books = self.__recommender.get_book_list()
        stats = self.__recommender.get_book_stats()
        self.__book_text.config(state='normal')
        self.__book_stats_text.config(state='normal')
        self.__book_text.delete(1.0, 'end')
        self.__book_stats_text.delete(1.0, 'end')
        self.__book_text.insert('end', books)
        self.__book_stats_text.insert('end', stats)
        self.__book_text.config(state='disabled')
        self.__book_stats_text.config(state='disabled')

    # ========================================================

    def run(self):
        self.__main_window.mainloop()


def main():
    myApp = RecommenderGUI()
    myApp.run()


main()
