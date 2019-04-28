import unittest
from unittest.mock import patch
from blog import Blog
import app


class PostTest(unittest.TestCase):
    # unittests
    def test_createclass(self):
        obj1 = Blog("Test", "Test Author")

        self.assertEqual(obj1.title, "Test")
        self.assertEqual(obj1.author, "Test Author")
        self.assertListEqual([], obj1.posts)

    def test_repr(self):
        obj1 = Blog("Test", "Test Author")
        obj2 = Blog("My Day", "Nathan")
        self.assertEqual(obj1.__repr__(), "Test by Test Author (0 posts)")
        self.assertEqual(obj2.__repr__(), "My Day by Nathan (0 posts)")

    def test_multiplepost(self):
        obj1 = Blog("Test", "Test Author")
        obj1.posts = ["Test"]
        obj2 = Blog("My Day", "Nathan")
        obj2.posts = ["test1", "testt2", "test3", "test4"]
        self.assertEqual(obj1.__repr__(), "Test by Test Author (1 post)")
        self.assertEqual(obj2.__repr__(), "My Day by Nathan (4 posts)")

    # integration tests
    def test_create_post_inblog(self):
        obj1 = Blog("Test", "Test Author")
        obj1.create_post('Test', 'Test Content')

        self.assertEqual(len(obj1.posts), 1)
        self.assertEqual(obj1.posts[0].title, 'Test')
        self.assertEqual(obj1.posts[0].content, 'Test Content')

    def test_json(self):
        obj1 = Blog("Test", "Test Author")
        obj1.create_post('Test', 'Test Content')

        expected = {
            "Title": "Test",
            "Author": "Test Author",
            "Posts": [
                {
                    "Title": "Test",
                    "Content": "Test Content"
                }
              ]
        }

        self.assertDictEqual(expected, obj1.json())

    def test_nojson(self):
        obj1 = Blog("Test", "Test Author")
        # obj1.create_post('Test', 'Test Content')

        expected = {

            "Title": "Test",
            "Author": "Test Author",
            "Posts": []
        }

        self.assertDictEqual(expected, obj1.json())

    """
    # system test
    def test_printblogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('-Test by Test Author (0 posts)')
    """
