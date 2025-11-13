import pytest
from services.cart_service import CartService
from typing import Dict, Any


def test_create_cart(cart_service: CartService):
    data: Dict[str, Any] = cart_service.create_cart()
    assert isinstance(data, dict), f"Expected a dictionary response, got {type(data)}"
    # 2. Key existence and type check (Standard API Response Structure)
    assert "id" in data, "Response data missing 'id' field."
    assert "type" in data, "Response data missing 'type' field."
    assert isinstance(data["id"], str), f"Expected 'id' to be a string, got {type(data['id'])}"
    assert isinstance(data["type"], str), f"Expected 'type' to be a string, got {type(data['type'])}"


    #Attributes validation
    attributes = data.get("attributes", {})

    print(attributes)


    assert isinstance(attributes,dict), f"Expected 'attributes' to be a dictionary, got {type(attributes)}"
    expected_keys_in_attributes = [
    "number", "item_total", "total", "subtotal_cents", "store_credit_total_cents",
    "total_cents", "total_minus_store_credits", "total_minus_store_credits_cents",
    "ship_total", "ship_total_cents", "adjustment_total", "created_at", "updated_at",
    "completed_at", "included_tax_total", "additional_tax_total", "display_additional_tax_total",
    "display_included_tax_total", "tax_total", "tax_total_cents", "currency", "state",
    "token", "email", "display_item_total", "display_ship_total", "display_adjustment_total",
    "display_tax_total", "promo_total", "display_promo_total", "promo_total_cents",
    "item_count", "special_instructions", "display_total", "display_total_minus_store_credits",
    "pre_tax_item_amount", "display_pre_tax_item_amount", "pre_tax_total",
    "display_pre_tax_total", "shipment_state", "payment_state"
]

    for key in expected_keys_in_attributes:
        assert  key in attributes, f"Missing expected attribute:{key}"



