import unittest
from blog import Blog


class PostTest(unittest.TestCase):
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
