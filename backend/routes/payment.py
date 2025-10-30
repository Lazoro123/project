from fastapi import APIRouter
import stripe, os
router = APIRouter()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "")

@router.post("/create-checkout-session")
def create_checkout_session():
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {"currency":"usd","product_data":{"name":"Cloud VM Access"},"unit_amount":1000},
            "quantity":1
        }],
        mode="payment",
        success_url="http://localhost:3000/success",
        cancel_url="http://localhost:3000/cancel"
    )
    return {"url": session.url}
