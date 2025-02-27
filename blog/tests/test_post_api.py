import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models.users import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="admin@admin.com", password="a/@1234567", is_verified=True
    )
    return user



# @pytest.mark.filterwarnings("error")
# @pytest.mark.filterwarnings("ignore:api-v1")
@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200_status(self, api_client):
        url = reverse('api-v1:post-list') 
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201_status(self, api_client, common_user):
        user = common_user
        api_client.force_authenticate(user=user)
        url = reverse("api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
        }
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(self, api_client, common_user ):
        user = common_user
        api_client.force_authenticate(user=user)
        url = reverse("api-v1:post-list")
        data = {
            
            "title": "test",
            "status": True,
        }        
       
        response = api_client.post(url, data)
        assert response.status_code == 400
