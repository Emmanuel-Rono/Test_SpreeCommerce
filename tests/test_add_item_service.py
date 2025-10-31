from services.cart_service import CartService
from typing import Dict, Any



def test_add_item_service(cart_service:CartService,cart_headers:Dict[str, str]):
    variant_id = "12345"
    quantity = 2

    add_item_service_response= cart_service.add_item(variant_id, quantity, cart_headers)

    assert isinstance(add_item_service_response, dict), f"Expected Dict got: {type(add_item_service_response)}"
