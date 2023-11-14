from django.test import TestCase
from django.urls import reverse

class SearchResultTests(TestCase):
    def test_get_search_results(self):
        response = self.client.get(reverse('search-results'))
        self.assertEqual(response.status_code, 200)

    def test_post_search_result(self):
        data = {"key": "value", "key2": "value2"} # replace with your data
        response = self.client.post(reverse('search-results'), data, content_type='application/json')
        self.assertEqual(response.status_code, 201)

