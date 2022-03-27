import json
import tempfile
from pathlib import Path

import mock
from django.core.files import File
from django.test import override_settings
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase


class TestCaseWithData(APITestCase):
    fixtures = ["my_fixture.json"]

    @classmethod
    def setUpTestData(cls):
        cls.url_post = reverse("file-list")
        cls.url_info = reverse("file-file_info")


class TestResponse(TestCaseWithData):
    def test_response_get_info(self):
        response = self.client.get(self.url_info)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_content: dict = json.loads(response.content)[0]
        response_keys = response_content.keys()
        self.assertIn("name", response_keys, int)
        self.assertIn("size", response_keys, int)
        self.assertIn("type", response_keys, str)
        self.assertIn("upload_data", response_keys, str)
        self.assertIn("file", response_keys, int)

        self.assertEqual(len(response_keys), 5)

    @override_settings(MEDIA_ROOT=Path(tempfile.gettempdir()))
    def test_send_file(self):
        image_mock = mock.MagicMock(spec=File)
        image_mock.name = "image.png"
        client = APIClient()
        client.post("/endpoint/", {"file": image_mock}, format="multipart")
