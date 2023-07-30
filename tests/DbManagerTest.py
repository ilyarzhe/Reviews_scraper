import datetime
import unittest
import psycopg2
from main.DbManager import DbManager
from main.Review import Review

class TestDbManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the test database connection
        cls.test_dbname = "ilyarzheznikov"
        cls.test_user = "test_user"
        cls.test_password = "test_password"
        cls.test_host = "localhost"
        cls.test_port = "5432"

        # Create a connection to the test database
        cls.connection = psycopg2.connect(dbname=cls.test_dbname, user=cls.test_user, password=cls.test_password,
                                          host=cls.test_host, port=cls.test_port)
        cls.connection.autocommit = True

    @classmethod
    def tearDownClass(cls):
        # Close the test database connection
        cls.connection.close()

    def setUp(self):
        # Create a DbManager instance for testing
        self.db_manager = DbManager(dbname=self.test_dbname, user=self.test_user, password=self.test_password,
                                    host=self.test_host, port=self.test_port)

    def tearDown(self):
        # Clean up test data after each test
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM reviews")
            cursor.execute("ALTER SEQUENCE reviews_id_seq RESTART WITH 1")

    def test_insert_review(self):
        # Test inserting a review into the database
        review = Review(rating=4.5, text="Test review", date="2023-07-30", summary="Test summary")
        self.db_manager.insert_review(review)

        # Query the database to verify that the review was inserted correctly
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM reviews")
            rows = cursor.fetchall()

        # Assert that the review was inserted correctly
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], "Test summary")
        self.assertEqual(rows[0][2], "Test review")
        self.assertEqual(rows[0][3], 4.5)
        self.assertEqual(rows[0][4], datetime.date(2023,7,30))

if __name__ == '__main__':
    unittest.main()
