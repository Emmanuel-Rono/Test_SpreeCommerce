# conftest.py fixture code only

import pytest
import requests
from typing import Dict, Any
from config.settings import settings
from services.cart_service import CartService


@pytest.fixture(scope="session")
def base_url() -> str:
    return settings.BASE_API_URL


@pytest.fixture(scope="session")
def api_client(base_url: str) -> requests.Session:
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/vnd.api+json",
        "Accept": "application/vnd.api+json"
    })
    return session


@pytest.fixture(scope="session")
def admin_headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {settings.ADMIN_AUTH_TOKEN}"
    }



@pytest.fixture(scope="session")
def customer_headers() -> Dict[str, str]:
    return {
        "Authorization": f"Bearer {settings.CUSTOMER_AUTH_TOKEN}"
    }


@pytest.fixture
def customer_cart(api_client: requests.Session, base_url: str) -> Dict[str, Any]:
    cart_endpoint = f"{base_url}/api/v2/storefront/cart"

    # SETUP
    response = api_client.post(cart_endpoint)
    assert response.status_code == 201

    response_data = response.json()["data"]
    cart_id = response_data["id"]
    order_token = response_data["attributes"]["token"]

    cart_auth_headers = {"X-Spree-Order-Token": order_token}

    cart_details = {
        "id": cart_id,
        "token": order_token,
        "headers": cart_auth_headers
    }

    yield cart_details
    # TEARDOWN
    delete_response = api_client.delete(cart_endpoint, headers=cart_auth_headers)
    if delete_response.status_code not in [204, 404]:
        pytest.fail(f"Failed to delete cart {cart_id} during teardown.")

@pytest.fixture(scope="session")
def cart_service(api_client:requests.Session, base_url:str) -> CartService:
        # 1. The instantiation happens here!
        service = CartService(
            client=api_client,
            base_url=base_url
        )
        return service




