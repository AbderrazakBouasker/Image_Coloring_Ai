import json
import pytest
from flask_testing import TestCase
from app import app
import os

class TestFlaskRoutes(TestCase):
    def create_app(self):
        return app

    def test_home_page(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assert_template_used('index.html')

    def test_results_page(self):
        response = self.client.get('/results')
        self.assert200(response)
        self.assert_template_used('results.html')

    def test_colorize_route(self):
        # load data.json
        with open("data.json") as file:
            data = json.load(file)
            print("test")
        with open('test_image.jpg', 'rb') as img:
            response = self.client.post('/colorize', content_type='multipart/form-data',
                                        data={'image': img}, follow_redirects=True)
        self.assert200(response)
        self.assert_template_used('index.html')

        # reload data.json to check if an entry was added
        with open("data.json") as file:
            new_data = json.load(file)
            self.assertEqual(len(new_data), len(data) + 1)

        # Check if the colorized_image_url parameter was passed to the template
        colorized_image_url = self.get_context_variable('colorized_image_url')
        self.assertIsNotNone(colorized_image_url)

if __name__ == '__main__':
    pytest.main()