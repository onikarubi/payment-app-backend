from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import stripe

app = FastAPI()

class PaymentIntentRequest(BaseModel):
    amount: int


@app.post("/create-payment-intent")
async def create_payment_intent(request: PaymentIntentRequest):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=request.amount, currency="usd"
        )
        return {"clientSecret": payment_intent.client_secret}
    except stripe.error.StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))
