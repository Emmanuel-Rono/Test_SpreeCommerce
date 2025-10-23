import pytest
from services.cart_service import CartService

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self._json_data = json_data
        self.status_code = status_code
    def raise_for_status(self): pass
    def json(self): return self._json_data

class MockClient:
    def post(self, url, json=None, headers=None):
        return MockResponse({"data": {"id": "cart123", "type": "cart"}})
    def get(self, url, headers=None):
        return MockResponse({"data": {"id": "cart123", "type": "cart"}})
    def delete(self, url, headers=None):
        return MockResponse({}, status_code=204)

@pytest.fixture
def cart_service():
    mock_client = MockClient()
    return CartService(mock_client, "https://demo.spreecommerce.org", "fake-token")

def test_create_cart(cart_service):
    data = cart_service.create_cart()
    assert isinstance(data, dict)
    assert data["id"] == "cart123"
    assert data["type"] == "cart"