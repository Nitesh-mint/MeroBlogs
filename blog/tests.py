from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


class PostTest(TestCase):

    # Class method to make the method static
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@email.com',
            password = 'testpass123',
        )
        cls.post = Post.objects.create(
            title = 'A Test Post',
            slug = 'a-test-post',
            author = cls.user,
            body = 'This is a body of the post',
        )

    def test_post_detail_view(self):
        response = self.client.get(self.post.get_absolute_url())
        no_response = self.client.get("post/1234/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A Test Post')
        self.assertContains(response, 'This is a body of the post')
        self.assertTemplateUsed(response, 'post/post_detail_view.html')

    def test_post_create_view(self):
        self.client.login(email='testuser@email.com', password='testpass123')
        post_data = {
            'title': 'Test Title from the test',
            'thumbnail': 'test-thumb.jpg',
            'category': 'test-category',
            'body': 'This is a test post.',
            'status': 'draft',
        }
        response = self.client.post(reverse('post_create'), post_data)
        print(response)
        self.assertEqual(response.status_code, 302)
        # new_post = Post.objects.get(title="Test Title from the test")
        # print(new_post)
        # self.assertTrue(Post.objects.filter(title='Test Title from the test', author=self.user).exists())

