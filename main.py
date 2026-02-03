from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 1. Definimos la "Forma" de los datos (El contrato)
# Esto obliga a quien nos envíe datos a cumplir estas reglas.
class PaymentRequest(BaseModel):
    card_number: str
    amount: float
    currency: str
    cvv: int

@app.get("/")
def read_root():
    return {"message": "Redsys Simulator Ready 💳"}

# 2. El Endpoint de Cobro (POST)
# Aquí es donde ocurre la magia. Recibimos una 'transaction'.
@app.post("/process-payment")
def process_payment(transaction: PaymentRequest):
    
    # --- LÓGICA DE NEGOCIO (Simulación) ---
    
    # Regla 1: Validar longitud de tarjeta (simulamos que deben ser 16 dígitos)
    if len(transaction.card_number) != 16:
        raise HTTPException(status_code=400, detail="❌ Tarjeta inválida: Debe tener 16 dígitos")

    # Regla 2: Simulamos fondos insuficientes si intenta cobrar más de 1000€
    if transaction.amount > 1000:
        return {
            "status": "denied",
            "reason": "Fondos insuficientes (Límite superado)",
            "transaction_id": None
        }

    # Si pasa todo, cobramos
    return {
        "status": "approved",
        "message": "✅ Pago realizado con éxito",
        "charged_amount": transaction.amount,
        "currency": transaction.currency
    }