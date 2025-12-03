from services.cart_service import CartService
from typing import Dict, Any

def test_add_item_service(cart_service:CartService):
    cart_service.create_cart()
    variant_id = "3"
    quantity = 2
    add_item_service_response= cart_service.add_item (variant_id, quantity)
    assert isinstance(add_item_service_response, dict), f"Expected Dict got: {type(add_item_service_response)}"

    expected_keys = {
        "id", "type", "attributes", "relationships"
    }
    for key in expected_keys:
        assert key in add_item_service_response.keys(), f"Key {key} not in add_item_service_response"

    expected_attr_keys = [
        "number", "item_total", "total", "subtotal_cents", "store_credit_total_cents",
        "total_cents", "total_minus_store_credits", "total_minus_store_credits_cents",
        "ship_total", "ship_total_cents", "adjustment_total", "created_at", "updated_at",
        "completed_at", "included_tax_total", "additional_tax_total", "display_additional_tax_total",
        "display_included_tax_total", "tax_total", "tax_total_cents", "currency", "state",
        "token", "email", "display_item_total", "display_ship_total", "display_adjustment_total",
        "display_tax_total", "promo_total", "display_promo_total", "promo_total_cents",
        "item_count", "special_instructions", "display_total", "display_total_minus_store_credits",
        "pre_tax_item_amount", "display_pre_tax_item_amount", "pre_tax_total",
        "display_pre_tax_total", "shipment_state", "payment_state"]

    attributes = add_item_service_response.get("attributes",{})
    for key in expected_attr_keys:
        assert key in attributes, f"Missing Attributes {key}"

    expected_rel_attributes = [
        "line_items", "variants", "promotions", "payments", "shipments",
        "user", "billing_address", "shipping_address"
    ]

    relationship = add_item_service_response.get("relationships",{})
    for key in expected_rel_attributes:
        assert key in relationship, f"{key} is not in expected_rel_attributes"
    assert type == add_item_service_response["type"]
