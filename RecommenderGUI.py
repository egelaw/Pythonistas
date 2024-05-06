# Authors: Ismail Gul and Endalkachew Bogale Gelaw
# Date: 05/05/2024
# Description: This is a GUI program for Recommender which perform an analysis of the specified data, generate statistics

import tkinter
from tkinter import ttk

import numpy as np

from Recommender import Recommender

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RecommenderGUI:
    def __init__(self):
        # Creates an instance of a Recommender object
        self.__recommender = Recommender()

        # Creates main window
        self.__main_window = tkinter.Tk()
        self.__main_window.title("Media Recommender")
        self.__main_window.geometry("1200x800")

        self.__notebook = ttk.Notebook(self.__main_window)

        # Frame for the buttons
        self.__buttons_frame = tkinter.Frame(self.__main_window)
        self.__buttons_frame.pack(side='bottom')

        # Buttons
        self.__load_shows_button = tkinter.Button(self.__buttons_frame, text='Load Shows', command=self.load_shows)
        self.__load_shows_button.pack(side='left', padx=75)

        self.__load_books_button = tkinter.Button(self.__buttons_frame, text='Load Books', command=self.load_books)
        self.__load_books_button.pack(side='left', padx=75)

        self.__load_associations_button = tkinter.Button(self.__buttons_frame, text='Load Recommendations', command=self.load_associations)
        self.__load_associations_button.pack(side='left', padx=75)

        self.__credit_info_button = tkinter.Button(self.__buttons_frame, text='Information', command=self.credit_info_box)
        self.__credit_info_button.pack(side='left', padx=75)

        self.quit_button = tkinter.Button(self.__buttons_frame, text='Quit', command=self.__main_window.quit)
        self.quit_button.pack(side='left', padx=75)

        # pack notebook
        self.__notebook.pack(expand=True, fill='both')

        # Movies tab
        self.__movie_tab = tkinter.Frame(self.__notebook)
        self.__notebook.add(self.__movie_tab, text='Movies')

        # Frame for the movie_text widget
        self.__movie_frame = tkinter.Frame(self.__movie_tab)

        # Frame for the movie_stats
        self.__movie_stats_frame = tkinter.Frame(self.__movie_tab)

        # pack frames
        self.__movie_frame.pack(expand=True, fill='both')
        self.__movie_stats_frame.pack(expand=True, fill='both')

        # Text widget to display the movie
        self.__movie_text = tkinter.Text(self.__movie_frame, wrap='word')

        # Default text to display
        self.__movie_text.insert(tkinter.END, "No movies have been loaded yet.")
        self.__movie_text.config(state='disabled')

        # Vertical scrollbar
        self.__scrollbar = tkinter.Scrollbar(self.__movie_frame, orient='vertical', command=self.__movie_text.yview)
        self.__scrollbar.pack(side='right', fill='y')

        self.__movie_text.config(yscrollcommand=self.__scrollbar.set)
        self.__movie_text.pack(expand=True, fill='both')

        # stats text for movies
        self.__movie_stats_text = tkinter.Text(self.__movie_stats_frame, wrap='word')
        self.__movie_stats_text.pack(expand=True, fill='both')
        self.__movie_stats_text.insert(tkinter.END, "No movies have been loaded yet.")
        self.__movie_stats_text.config(state='disabled')

        # TV Shows tab
        self.__TV_show_tab = tkinter.Frame(self.__notebook)
        self.__notebook.add(self.__TV_show_tab, text='TV Shows')

        # Frame for the TV_show_text widget
        self.__TV_show_frame = tkinter.Frame(self.__TV_show_tab)

        # Frame for the TV_show_stats
        self.__TV_show_stats_frame = tkinter.Frame(self.__TV_show_tab)

        # Pack frames
        self.__TV_show_frame.pack(expand=True, fill='both')
        self.__TV_show_stats_frame.pack(expand=True, fill='both')

        # Text widget to display the TV_show
        self.__TV_show_text = tkinter.Text(self.__TV_show_frame, wrap='word')

        # Default text to display
        self.__TV_show_text.insert(tkinter.END, "No TV_shows have been loaded yet.")
        self.__TV_show_text.config(state='disabled')

        # Vertical scrollbar
        self.__scrollbar = tkinter.Scrollbar(self.__TV_show_frame, orient='vertical', command=self.__TV_show_text.yview)
        self.__scrollbar.pack(side='right', fill='y')

        self.__TV_show_text.config(yscrollcommand=self.__scrollbar.set)
        self.__TV_show_text.pack(expand=True, fill='both')

        # stats text for TV_show
        self.__TV_show_stats_text = tkinter.Text(self.__TV_show_stats_frame, wrap='word')
        self.__TV_show_stats_text.pack(expand=True, fill='both')
        self.__TV_show_stats_text.insert(tkinter.END, "No TV_shows have been loaded yet.")
        self.__TV_show_stats_text.config(state='disabled')

        # Books tab
        self.__book_tab = tkinter.Frame(self.__notebook)
        self.__notebook.add(self.__book_tab, text='Books')

        # Frame for the book_text widget
        self.__book_frame = tkinter.Frame(self.__book_tab)

        # Frame for the book_stats
        self.__book_stats_frame = tkinter.Frame(self.__book_tab)

        # Pack frames
        self.__book_frame.pack(expand=True, fill='both')
        self.__book_stats_frame.pack(expand=True, fill='both')

        # Text widget to display the books
        self.__book_text = tkinter.Text(self.__book_frame, wrap='word')

        # Default text to display
        self.__book_text.insert(tkinter.END, "No books have been loaded yet.")
        self.__book_text.config(state='disabled')

        # Vertical scrollbar
        self.__scrollbar = tkinter.Scrollbar(self.__book_frame, orient='vertical', command=self.__book_text.yview)
        self.__scrollbar.pack(side='right', fill='y')

        self.__book_text.config(yscrollcommand=self.__scrollbar.set)
        self.__book_text.pack(expand=True, fill='both')

        # stats text for books
        self.__book_stats_text = tkinter.Text(self.__book_stats_frame, wrap='word')
        self.__book_stats_text.pack(expand=True, fill='both')
        self.__book_stats_text.insert(tkinter.END, "No books have been loaded yet.")
        self.__book_stats_text.config(state='disabled')

        # Search Movies/TV tab
        self.__search_show_tab = tkinter.Frame(self.__notebook)
        self.__notebook.add(self.__search_show_tab, text='Search Movies/TV')

        self.__show_type_frame = tkinter.Frame(self.__search_show_tab)
        self.__show_type_frame.pack(fill='both')
        self.__show_type_label = tkinter.Label(self.__show_type_frame, text="Type:")
        self.__show_type_label.pack(side='left')

        self.__search_type_var = tkinter.StringVar()
        self.__search_type_var.set("Movie")
        self.__search_type_combobox = ttk.Combobox(self.__show_type_frame, textvariable=self.__search_type_var, values=["Movie", "TV Show"],)
        self.__search_type_combobox.pack(side='left')

        # Title, Director, Actor and Genre frames
        self.__show_title_frame = tkinter.Frame(self.__search_show_tab)
        self.__show_title_frame.pack(fill='both')
        self.__show_director_frame = tkinter.Frame(self.__search_show_tab)
        self.__show_director_frame.pack(fill='both')
        self.__show_actor_frame = tkinter.Frame(self.__search_show_tab)
        self.__show_actor_frame.pack(fill='both')
        self.__show_genre_frame = tkinter.Frame(self.__search_show_tab)
        self.__show_genre_frame.pack(fill='both')

        # Title label and entry for Show
        self.__show__title_search_entry_label = tkinter.Label(self.__show_title_frame, text="Title:")
        self.__show__title_search_entry_label.pack(side='left')
        self.__show_title_search_entry = tkinter.Entry(self.__show_title_frame, width=70)
        self.__show_title_search_entry.pack(side='left', fill='x')

        # Director label and entry for Show
        self.__show_director_entry_label = tkinter.Label(self.__show_director_frame, text="Director:")
        self.__show_director_entry_label.pack(side='left')
        self.__show_director_entry = tkinter.Entry(self.__show_director_frame, width=70)
        self.__show_director_entry.pack(side='left', fill='x')

        # Actor label and entry for Show
        self.__show_actor_entry_label = tkinter.Label(self.__show_actor_frame, text="Actor:")
        self.__show_actor_entry_label.pack(side='left')
        self.__show_actor_entry = tkinter.Entry(self.__show_actor_frame, width=70)
        self.__show_actor_entry.pack(side='left', fill='x')

        # Genre label and entry for Show
        self.__show_genre_entry_label = tkinter.Label(self.__show_genre_frame, text="Genre:")
        self.__show_genre_entry_label.pack(side='left')
        self.__show_genre_entry = tkinter.Entry(self.__show_genre_frame, width=70)
        self.__show_genre_entry.pack(side='left', fill='x')

        # Search button
        self.__show_search_button = tkinter.Button(self.__search_show_tab, text="Search", command=self.search_shows)
        self.__show_search_button.pack(anchor='w')

        # Search results text area
        self.__show_search_results_text = tkinter.Text(self.__search_show_tab, wrap='word')
        self.__show_search_results_text.pack(fill='both', expand=True, padx=5, pady=5)
        self.__show_search_results_text.insert(tkinter.END, "Perform a search to see results.")
        self.__show_search_results_text.config(state='disabled')

        # a vertical scrollbar
        self.__search_show_scrollbar = tkinter.Scrollbar(self.__show_search_results_text, orient='vertical', command=self.__show_search_results_text.yview)
        self.__search_show_scrollbar.pack(side='right', fill='y')

        # Search Books
        self.__search_book_tab = tkinter.Frame(self.__notebook)
        self.__notebook.add(self.__search_book_tab, text='Search Books')

        # Title, Author, and Publisher frames
        self.__book_title_frame = tkinter.Frame(self.__search_book_tab)
        self.__book_title_frame.pack(fill='both')
        self.__book_author_frame = tkinter.Frame(self.__search_book_tab)
        self.__book_author_frame.pack(fill='both')
        self.__book_publisher_frame = tkinter.Frame(self.__search_book_tab)
        self.__book_publisher_frame.pack(fill='both')

        # Title label and entry for Book
        self.__book_search_entry_label = tkinter.Label(self.__book_title_frame, text="Title:")
        self.__book_search_entry_label.pack(side='left')
        self.__book_search_entry = tkinter.Entry(self.__book_title_frame, width=70)
        self.__book_search_entry.pack(side='left', fill='x')

        # Author label and entry for Book
        self.__book_author_entry_label = tkinter.Label(self.__book_author_frame, text="Author:")
        self.__book_author_entry_label.pack(side='left')
        self.__book_author_entry = tkinter.Entry(self.__book_author_frame, width=70)
        self.__book_author_entry.pack(side='left', fill='x')

        # Publisher label and entry for Book
        self.__book_publisher_entry_label = tkinter.Label(self.__book_publisher_frame, text="Publisher:")
        self.__book_publisher_entry_label.pack(side='left')
        self.__book_publisher_entry = tkinter.Entry(self.__book_publisher_frame, width=70)
        self.__book_publisher_entry.pack(side='left', fill='x')

        # Search button
        self.__book_search_button = tkinter.Button(self.__search_book_tab, text="Search", command=self.search_books)
        self.__book_search_button.pack(anchor='w')

        # Search results text area
        self.__book_search_results_text = tkinter.Text(self.__search_book_tab, wrap='word')
        self.__book_search_results_text.pack(fill='both', expand=True, padx=5, pady=5)
        self.__book_search_results_text.insert(tkinter.END, "Perform a search to see results.")
        self.__book_search_results_text.config(state='disabled')

        # a vertical scrollbar
        self.__search_book_scrollbar = tkinter.Scrollbar(self.__book_search_results_text, orient='vertical', command=self.__book_search_results_text.yview)
        self.__search_book_scrollbar.pack(side='right', fill='y')

        # Media Recommendation tab
        self.__recom_tab = tkinter.Frame(self.__notebook)
        self.__notebook.add(self.__recom_tab, text="Recommendations")
        
        # Combobox with the options Movie, TV Show, Book
        self.__recom_type_frame = tkinter.Frame(self.__recom_tab)
        self.__recom_type_frame.pack(fill='both')
        self.__recom_type_label = tkinter.Label(self.__recom_type_frame, text="Type:")
        self.__recom_type_label.pack(side='left')
        self.__recom_type_var = tkinter.StringVar()
        self.__recom_type_var.set("Movie")
        self.__recom_type_combobox = ttk.Combobox(self.__recom_type_frame, textvariable=self.__recom_type_var, values=["Movie", "TV Show", "Book"])
        self.__recom_type_combobox.pack(side='left')

        # Appropriate Label and Entry widgets for title
        self.__recom_title_frame = tkinter.Frame(self.__recom_tab)
        self.__recom_title_frame.pack(fill='both')
        self.__recom_title_label = tkinter.Label(self.__recom_title_frame, text="Title:")
        self.__recom_title_label.pack(side='left')
        self.__recom_title_entry = tkinter.Entry(self.__recom_title_frame, width=70)
        self.__recom_title_entry.pack(side='left', fill='x')

        # Button for the recommendation search
        self.__recom_search_button = tkinter.Button(self.__recom_tab, text="Get Recommendation", command=self.get_recommendations)
        self.__recom_search_button.pack(anchor='w')

        # Default text
        self.__recom_text = tkinter.Text(self.__recom_tab, wrap='word')
        self.__recom_text.pack(fill='both', expand=True, padx=5, pady=5)
        self.__recom_text.insert(tkinter.END, "Enter a title to receive a recommendation.")
        self.__recom_text.config(state='disabled')

        # Scroll bar
        self.__recom_scrollbar = tkinter.Scrollbar(self.__recom_text, orient='vertical', command=self.__recom_text.yview)
        self.__recom_scrollbar.pack(side='right', fill='y')   

        # Ratings tab
        self.__rating_tab = tkinter.Frame(self.__notebook)
        self.__notebook.add(self.__rating_tab, text='Ratings')

        # Reference to the canvas widgets
        self.__movie_canvas = None
        self.__tv_canvas = None

    # Define the load_shows method
    def load_shows(self):

        # Clear old figures
        if self.__movie_canvas is not None:
            self.__movie_canvas.get_tk_widget().pack_forget()
        if self.__tv_canvas is not None:
            self.__tv_canvas.get_tk_widget().pack_forget()

        self.__recommender.load_shows()

        movies = self.__recommender.get_movie_list()
        movies_stats, movie_rating_dict = self.__recommender.get_movie_stats()
        self.__movie_text.config(state='normal')
        self.__movie_stats_text.config(state='normal')
        self.__movie_text.delete(1.0, 'end')
        self.__movie_stats_text.delete(1.0, 'end')
        self.__movie_text.insert('end', movies)
        self.__movie_stats_text.insert('end', movies_stats)
        self.__movie_text.config(state='disabled')
        self.__movie_stats_text.config(state='disabled')

        tv_shows = self.__recommender.get_tv_list()
        tv_shows_stats, tv_rating_dict = self.__recommender.get_tv_stats()
        self.__TV_show_text.config(state='normal')
        self.__TV_show_stats_text.config(state='normal')
        self.__TV_show_text.delete(1.0, 'end')
        self.__TV_show_stats_text.delete(1.0, 'end')
        self.__TV_show_text.insert('end', tv_shows)
        self.__TV_show_stats_text.insert('end', tv_shows_stats)
        self.__TV_show_text.config(state='disabled')
        self.__TV_show_stats_text.config(state='disabled')

        movie_fig, ax = plt.subplots()
        ax.pie(list(movie_rating_dict.values()), labels=list(movie_rating_dict.keys()),
               autopct='%1.2f%%', startangle=90, colors=plt.cm.viridis(np.linspace(0, 1, len(movie_rating_dict))))
        ax.axis('equal')
        ax.set_title("Movie Ratings")
        ax.legend(movie_rating_dict.keys(), title="Ratings", loc="upper right")

        tv_fig, ax = plt.subplots()
        ax.pie(list(tv_rating_dict.values()), labels=list(tv_rating_dict.keys()),
               autopct='%1.2f%%', startangle=90, colors=plt.cm.viridis(np.linspace(0, 1, len(tv_rating_dict))))
        ax.axis('equal')
        ax.set_title("TV Show Ratings")
        ax.legend(tv_rating_dict.keys(), title="Ratings", loc="upper right")

        # Create a FigureCanvasTkAgg object for each figure
        self.__movie_canvas = FigureCanvasTkAgg(movie_fig, master=self.__rating_tab)
        self.__tv_canvas = FigureCanvasTkAgg(tv_fig, master=self.__rating_tab)

        # Display the canvases
        self.__movie_canvas.draw()
        self.__movie_canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)

        self.__tv_canvas.draw()
        self.__tv_canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)

    # Define the load_associations method
    def load_associations(self):
        self.__recommender.load_associations()
    
    # Define the load_books method
    def load_books(self):
        self.__recommender.load_books()
        books = self.__recommender.get_book_list()
        stats = self.__recommender.get_book_stats()
        self.__book_text.config(state='normal')
        self.__book_stats_text.config(state='normal')
        self.__book_text.delete(1.0, 'end')
        self.__book_stats_text.delete(1.0, 'end')
        try:
            self.__book_text.insert('end', books)
        except tkinter.TclError:  # In case the user closes the window
            # In case nothing is passed (e.g., loading is canceled)
            return  # Do nothing
        self.__book_stats_text.insert('end', stats)
        self.__book_text.config(state='disabled')
        self.__book_stats_text.config(state='disabled')
    
    # Show information about team members and project completion date
    def credit_info_box(self):
        group_members = ["Ismail Gul", "Enalkachew Gelaw"]
        completion_day = "May 7th, 2024"
        
        # Create the message
        message = "Group Members:\n\n"
        for member in group_members:
            message += f"- {member}\n"
        message += f"\nProject completed on: {completion_day}"
        
        # Show messagebox
        tkinter.messagebox.showinfo("Credit Information", message)

    # Define the search_shows method
    def search_shows(self):
        show_type = self.__search_type_combobox.get()
        show_title = self.__show_title_search_entry.get()
        show_director = self.__show_director_entry.get()
        show_actor = self.__show_actor_entry.get()
        show_genre = self.__show_genre_entry.get()

        results = self.__recommender.search_TV_Movies(show_type, show_title, show_director, show_actor, show_genre)

        # Clear the text widget before inserting new results
        self.__show_search_results_text.config(state='normal')
        self.__show_search_results_text.delete(1.0, 'end')

        # Insert the search results into the text widget
        self.__show_search_results_text.insert("end", results)
        self.__show_search_results_text.config(state='disabled')

    # Define the search_books method
    def search_books(self):
        book_title = self.__book_search_entry.get()
        book_author = self.__book_author_entry.get()
        book_publisher = self.__book_publisher_entry.get()
        results = self.__recommender.search_books(book_title, book_author, book_publisher)

        # Clear the text widget
        self.__book_search_results_text.config(state='normal')
        self.__book_search_results_text.delete(1.0, 'end')

        # Insert the search results
        self.__book_search_results_text.insert("end", results)
        self.__book_search_results_text.config(state='disabled')
        
    # Method to display recommendations in the text area
    def get_recommendations(self):
        type = self.__recom_type_var.get()
        title = self.__recom_title_entry.get()
        
        # Get recommendations
        recommendations = self.__recommender.get_recommendations(type, title)
        
        # Display the result in the text area
        self.__recom_text.config(state='normal')
        self.__recom_text.delete(1.0, 'end')
        self.__recom_text.insert("end", recommendations)
        self.__recom_text.config(state='disabled')

    # Main loop function
    def run(self):
        self.__main_window.mainloop()

# Main function
def main():
    myApp = RecommenderGUI()
    myApp.run()

# Call the main function
if __name__ == '__main__':
    main()