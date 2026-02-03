# 💳 Payment Gateway Simulator (v2.0: With Persistence)

## 🤔 Why did I build this?
Have you ever wondered what actually happens in those few seconds after you hit the "Pay" button on a website? As someone aiming to dive into the **Fintech** world and Backend development, I didn't want to just use a library—I wanted to build the logic from scratch.

This project simulates the "brain" behind a payment processor, handling validation, logic, and storage.

## 🚀 🆕 Update v2.0: The "Mid-Level" Upgrade
I recently refactored the project to move from a basic script to a robust backend system.
* **Real Persistence (SQL):** Integrated **SQLite** and **SQLAlchemy**. Transactions are now permanently saved in a database file (`payments.db`), meaning data survives server restarts (unlike the previous in-memory version).
* **Security & Privacy (PCI-DSS principles):** Implemented **Data Masking**. The database *never* stores the full credit card number, only the last 4 digits (e.g., `4444`). This mimics real-world GDPR and security compliance.
* **Audit Endpoint:** Added `GET /history` to query the persistent database.

## ⚙️ How it works (The Business Logic)
I've programmed real-world constraints to mimic how actual banks operate:

1.  **The Gatekeeper (Validation):** Before even touching the database, the system checks if the data makes sense using **Pydantic**.
2.  **The Banker (Decision Logic):**
    * ✅ **Approved:** Valid card + reasonable amount.
    * ⛔ **Insufficient Funds:** Charges over **2,000€** are automatically rejected.
3.  **The Vault (Storage):** If approved, the transaction is hashed and safely stored in the SQL database for future auditing.

## 🛠️ Tech Stack (The "Why")
* **Python 3.10:** My core language.
* **FastAPI:** Chosen for high performance and automatic documentation.
* **SQLAlchemy ORM:** Used to manage database transactions professionally, avoiding raw SQL queries.
* **SQLite:** A serverless SQL engine for local persistence.
* **Pydantic:** For strict data validation.

## 🚀 Take it for a spin

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/Anguis400/payment-gateway-api.git](https://github.com/Anguis400/payment-gateway-api.git)
    cd payment-gateway-api
    ```

2.  **Install dependencies (Updated):**
    ```bash
    pip install fastapi uvicorn sqlalchemy
    ```

3.  **Fire up the engine:**
    ```bash
    uvicorn main:app --reload
    ```
    *Note: This will automatically generate the `payments.db` file in your folder.*

4.  **Interactive Testing:**
    Go to `http://127.0.0.1:8000/docs`.
    * Try `POST /process-payment` to make a transaction.
    * Restart the server.
    * Try `GET /history` to see that your data **survived**!

## 🧠 What I learned
Building v2.0 taught me the importance of **Data Persistence**. It's easy to make a script work in RAM, but connecting an API to a SQL database via an ORM (Object Relational Mapper) is what makes an application "production-ready". Also, learning to hide sensitive data (Masking) made me realize how critical privacy is in Fintech.

---
*Built with ⌨️, code, and caffeine by **Anguis400**.*