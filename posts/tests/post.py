from django.contrib.auth import get_user_model
from django.test import TestCase
from posts.models import Post


User = get_user_model()


class PostModelTestCase(TestCase):
    """

    """
    def setUp(self):
        """

        :return:
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass',
        )
        self.post = Post.objects.create(
            user_id=self.user,
            title='Test Post',
            caption='This is a test post.',
            is_active=True,
            likes_count=1
        )

    def test_is_like_by_user(self):
        """

        :return:
        """
        self.assertFalse(self.post.is_like_by_user(self.user))
        self.post.likes.create(user=self.user)
        self.assertTrue(self.post.is_like_by_user(self.user))

    def test_add_like(self):
        """

        :return:
        """
        self.post.add_like()
        self.assertEqual(self.post.likes_count, 2)

    def test_remove_like(self):
        """

        :return:
        """
        self.assertEqual(self.post.likes_count, 1)
        self.post.remove_like()
        self.assertEqual(self.post.likes_count, 0)
        self.post.remove_like()
        self.assertEqual(self.post.likes_count, 0)

