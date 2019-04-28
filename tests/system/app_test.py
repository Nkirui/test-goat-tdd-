import unittest
from unittest.mock import patch
from blog import Blog
import app


class PostTest(unittest.TestCase):

    # system test
    def test_printblogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('-Test by Test Author (0 posts)')

    def test_menu_prints_prompts(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)
