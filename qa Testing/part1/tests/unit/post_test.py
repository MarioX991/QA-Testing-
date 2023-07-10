"""
This script contains tests for script the post
"""

from unittest import TestCase
from post import Post
from datetime import datetime


class PostTest(TestCase):
    """
    This class containts folowing tests:
    - test_create_post
    - test_json_method
    """

    def setUp(self) -> None:
        self.post1 = Post("Test", "Test Content")

    def test_create_post(self):
        self.assertEqual("Test", self.post1.title)
        self.assertEqual("Test Content", self.post1.content)

    def test_json_method(self):
        # arrange
        post = self.post1
        current_data = datetime.today().strftime('%Y-%m-%d')
        expected_output = {'content': 'Test Content', 'title': 'Test'}
        # act
        json = post.json()
        # assert
        self.assertDictEqual(json, expected_output)
