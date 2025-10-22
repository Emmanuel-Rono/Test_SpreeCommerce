import requests


def test_create_cart(customer_cart, api_client, base_url):

    cart_endpoint = f"{base_url}/api/v2/storefront/cart"
    response_of_create_cart =requests.post(cart_endpoint)
    assert response_of_create_cart.status_code == 201
    print(response_of_create_cart.json())






