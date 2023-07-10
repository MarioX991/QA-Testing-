"""
 The Integratin the has been used whan we have a dependency or interaction inside the method that we are try to test.
 B = f(A) to make a test for B we have to invoke A, and this go over the boundary of unittest(we test just single function).
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

    def test_create_post_in_blog_method(self):
        # arrange
        blog = self.blog1
        # act
        blog.create_post("Test Post", "Test Content")
        # assert
        self.assertEqual(len(blog.posts), 1)
        self.assertEqual(blog.posts[0].title, "Test Post")
        self.assertEqual(blog.posts[0].content, "Test Content")

    def test_json(self):
        # arrange
        blog = self.blog1
        blog.create_post("Test Post", "Test Content")
        expectated = {
                     "title": "Test",
                     "author":"Test Author",
                     "posts": [{"title": "Test Post",
                                "content": "Test Content"}]
                     }
        # act
        # assert
        self.assertDictEqual(blog.json(),expectated)

    def test_json_no_posts(self):
        # arrange
        blog = self.blog1
        expectated = {
            "title": "Test",
            "author": "Test Author",
            "posts": []
        }
        # act
        # assert
        self.assertDictEqual(blog.json(), expectated)
