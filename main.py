from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from datetime import datetime

# --- 1. CONFIGURACIÓN DE BASE DE DATOS (NIVEL PRO) ---
# Creamos un archivo 'payments.db' que será nuestra base de datos real
DATABASE_URL = "sqlite:///./payments.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- 2. MODELO DE DATOS (LA TABLA SQL) ---
# Esto le dice a Python cómo crear la tabla en la base de datos
class TransactionDB(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String, index=True)
    amount = Column(Float)
    currency = Column(String)
    status = Column(String) # 'approved' o 'denied'
    date = Column(String)

# Creamos las tablas automáticamente al arrancar
Base.metadata.create_all(bind=engine)

# --- 3. MODELOS PYDANTIC (VALIDACIÓN) ---
class PaymentRequest(BaseModel):
    card_number: str
    amount: float
    currency: str
    cvv: int

# --- 4. INYECCIÓN DE DEPENDENCIAS ---
# Esto es muy Mid-Level: Una función para coger y soltar la conexión a la DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/process-payment")
def process_payment(transaction: PaymentRequest, db: Session = Depends(get_db)):
    
    # Lógica de Negocio (Igual que antes)
    status = "approved"
    
    if len(transaction.card_number) != 16:
        raise HTTPException(status_code=400, detail="❌ Tarjeta inválida")
    
    if transaction.amount > 2000:
        status = "denied" # Fondos insuficientes

    # --- AQUÍ OCURRE LA MAGIA MID-LEVEL ---
    # En lugar de solo devolver el JSON, guardamos en la Base de Datos
    new_transaction = TransactionDB(
        card_number=transaction.card_number[-4:], # Guardamos solo los últimos 4 dígitos por seguridad (GDPR)
        amount=transaction.amount,
        currency=transaction.currency,
        status=status,
        date=str(datetime.now())
    )
    
    db.add(new_transaction) # Preparamos
    db.commit()             # Guardamos permanentemente
    db.refresh(new_transaction) # Recargamos para obtener el ID generado

    return {
        "status": status,
        "transaction_id": new_transaction.id, # ¡Ahora devolvemos un ID real de base de datos!
        "message": "Transaction saved to Database 💾"
    }

@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    # Un endpoint extra para ver el historial guardado
    return db.query(TransactionDB).all()