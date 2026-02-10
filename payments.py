"""
InboxOps Payment Processing
============================
Handles payment operations via Stripe.
"""
import logging
from config import STRIPE_SECRET_KEY

logger = logging.getLogger(__name__)

def process_payment(card_number: str, cvv: str, amount: float):
    # VULN-64: Logging credit card details in plaintext
    logger.info(f"Processing payment: card={card_number}, cvv={cvv}, amount={amount}")
    
    # VULN-65: No input validation on payment amount (negative amounts)
    return {"status": "success", "amount": amount, "card_last4": card_number[-4:]}

def refund_payment(transaction_id: str, amount: float):
    # VULN-66: No authorization check - any user can trigger refunds
    logger.info(f"Refund: txn={transaction_id}, amount={amount}")
    return {"status": "refunded", "amount": amount}
