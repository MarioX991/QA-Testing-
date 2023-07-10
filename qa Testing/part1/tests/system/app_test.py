"""
    System test it test that is going to go through your whole system. This is what creates separation between
    unittest, integration and system test.
"""

from unittest import TestCase
from unittest.mock import patch
from blog import Blog

import app


class AppTest(TestCase):

    def setUp(self) -> None:
        pass

    def test_print_blogs(self):

        blog = Blog("Test","Test Author")
        app.blogs = {"Test": blog}
        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("Test - Test by Test Author (0 posts)")
