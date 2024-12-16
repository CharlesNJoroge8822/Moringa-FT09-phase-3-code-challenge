from database.connection import get_db_connection  # database connection
from models.author import Author  # the Author class
from models.magazine import Magazine  # the Magazine class

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):  
        """
        Initialize an Article instance.
        :param id: int, unique identifier for the article.
        :param title: str, title of the article.
        :param content: str, content of the article.
        :param author_id: int, ID of the associated author.
        :param magazine_id: int, ID of the associated magazine.
        """
        if not all([id, title, content, author_id, magazine_id]):
            raise ValueError("All fields (id, title, content, author_id, magazine_id) are required.")
        
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self): 
        """
        Return a string representation of the Article instance.
        """
        return f"<Article {self.title}>"

    @property
    def author(self):
        """
        Retrieve the author of the article from the database.
        :return: Author instance or None if not found.
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM authors WHERE id = ?', (self.author_id,))
            author_data = cursor.fetchone()
        
        if author_data:
            return Author(author_data['id'], author_data['name'])
        return None

    @property
    def magazine(self):
        """
        Retrieve the magazine of the article from the database.
        :return: Magazine instance or None if not found.
        """
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM magazines WHERE id = ?', (self.magazine_id,))
            magazine_data = cursor.fetchone()
        
        if magazine_data:
            return Magazine(magazine_data['id'], magazine_data['name'], magazine_data['category'])
        return None
