import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    
    # Test author creation
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")
    
    # Test article creation
    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")
    
    # Test valid magazine creation
    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    # Test magazine creation with invalid name length
    def test_invalid_magazine_name(self):
        # Name too short
        with self.assertRaises(ValueError):
            Magazine(2, "A", "Technology")  # Name is too short
        
        # Name too long
        with self.assertRaises(ValueError):
            Magazine(3, "This is a really long magazine name", "Technology")  # Name is too long

    # Test magazine creation with empty category
    def test_empty_category(self):
        with self.assertRaises(ValueError):
            Magazine(4, "Tech Weekly", "")  # Empty category

if __name__ == "main":
    unittest.main()
    