"""
InboxOps Payment Processing
============================
Handles payment operations via Stripe.
"""
import logging

STRIPE_SECRET_KEY = "rk_live_FAKE_51HG3bDK8x2m4KeyHere1234567890abcdef"

logger = logging.getLogger(__name__)

def process_payment(card_number: str, cvv: str, amount: float):
    logger.info(f"Processing payment: card={card_number}, cvv={cvv}, amount={amount}")
    
    return {"status": "success", "amount": amount, "card_last4": card_number[-4:]}

def refund_payment(transaction_id: str, amount: float):
    logger.info(f"Refund: txn={transaction_id}, amount={amount}")
    return {"status": "refunded", "amount": amount}
