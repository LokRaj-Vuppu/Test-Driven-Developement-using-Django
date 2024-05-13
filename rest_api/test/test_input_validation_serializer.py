from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_api.serializers import InputValidationserializer
from rest_framework import status


class TestInputValidations(APITestCase):

    def test_input_serializer_validation(self):
        client = APIClient()
        url = reverse("input_validation_with_serializer")
        input_data = {
            "name": "Raj kumar",
            "age": 23,
            "city": "Bengaluru",
            "state": "Karnataka",
            "country": "India",
            "mobile": "1213131",
        }
        data_after_validation = InputValidationserializer(data=input_data)

        self.assertTrue(data_after_validation.is_valid(), 'Input validation failed')

        response = client.post(url, input_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK, 'Status code not matched')
        # self.assertEqual()
