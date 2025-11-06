# services/cart_service.py
from typing import Dict, Any, Optional
import requests


class CartService:
    """
    Servic class to handle all Storefront API operations related to the shopping cart.
    Uses dependency injection for client and base URL.
    """

    def __init__(self, client: requests.Session, base_url: str, cart_token:Optional[str] = None) -> None:
        self.client = client
        self.base_url = base_url
        self.cart_endpoint = f"{self.base_url}/api/v2/storefront/cart"
        self.cart_token = cart_token
        self.cart_headers = {
            "Content-Type": "application/vnd.api+json",
            "Accept": "application/vnd.api+json"
        }
        self._update_headers_from_token()

    def _update_headers_from_token(self) -> None:
        if self.cart_token:
            self.cart_headers["X-Spree-Order-Token"] = self.cart_token
        else:
                self.cart_headers = {}


    def create_cart(self) -> Dict[str, Any]:
        create_cart_response = self.client.post(self.cart_endpoint)
        create_cart_response.raise_for_status()
        # Extract token from response attributes if present
        data=create_cart_response.json()["data"]
        token = data.get("attributes", {}).get("token")
        if token:
            self.cart_token = token
            self._update_headers_from_token()

        return create_cart_response.json()["data"]

    def get_cart(self,)-> Dict[str, Any]:
        get_cart_response = requests.get(self.cart_endpoint,
                                         headers=self.cart_headers
                                         )
        get_cart_response.raise_for_status()
        return get_cart_response.json()["data"]

    def add_item(self, variant_id: str, quantity: int) -> Dict[str, Any]:
        """Adds a product variant to the cart."""
        payload = {
            "variant_id": variant_id,
            "quantity": quantity
        }
        response = self.client.post(f"{self.cart_endpoint}/add_item", json=payload, headers=self.cart_headers)
        response.raise_for_status()
        return response.json()["data"]

    def remove_item(self, item_id: str, cart_headers: Dict[str, str]) -> bool:
        """Removes a line item from the cart."""
        response = self.client.delete(f"{self.cart_endpoint}/items/{item_id}", headers=cart_headers)
        if response.status_code == 200:
            return True
        response.raise_for_status()
        return True  # will not reach here if error

    def clear_cart(self, cart_headers: Dict[str, str]) -> bool:
        """Deletes the entire cart."""
        response = self.client.delete(self.cart_endpoint, headers=cart_headers)
        return response.status_code in [204, 404]  # 404 is acceptable if already deleted