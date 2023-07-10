"""
This script contains tests for script the post
"""

from unittest import TestCase
from post import Post
from blog import Blog
from datetime import datetime


class BlogTest(TestCase):
    """
    This class containts folowing tests:
    - test_create_post
    - test_json_method
    """

    def setUp(self) -> None:
        self.blog1 = Blog("Test", "Test Author")
        self.blog2 = Blog("My Day", "Rolf")

    def test_blog(self):
        # arrange
        blog = self.blog1
        # assert
        self.assertEqual("Test", blog.title)
        self.assertEqual("Test Author", blog.author)
        self.assertLessEqual([], blog.posts)

    def test_repr(self):
        # assert
        post = self.blog1
        output_expectation = "Test by Test Author (0 posts)"
        # act
        repr_method= post.__repr__()
        # assert
        self.assertEqual(repr_method,output_expectation)

    def test_repr_multiple_posts(self):
        post1 = self.blog1
        post2 = self.blog2
        output_exp = {"blog1": "Test by Test Author (1 post)",
                      "blog2": "My Day by Rolf (2 posts)"}
        post1.posts = ["test"]
        post2.posts=["test","runner"]

        self.assertEqual(post1.__repr__(), output_exp["blog1"])
        self.assertEqual(post2.__repr__(), output_exp["blog2"])



