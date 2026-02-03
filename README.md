💳 The Payment Logic Lab | A "Mini-Redsys" Simulator
🤔 Why did I build this?
Have you ever wondered what actually happens in those few seconds after you hit the "Pay" button on a website? As someone aiming to dive into the Fintech world and Backend development, I didn't want to just use a library—I wanted to build the logic from scratch.

This project is a simulation of the "brain" behind a payment processor. It handles the critical moment when a transaction is either welcomed with a green light or stopped at the gate.

⚙️ How it works (The Business Logic)
This isn't just a basic API that says "OK" to everything. I've programmed real-world constraints to mimic how actual banks operate:

The Gatekeeper (Validation): Before even touching the "vault," the system checks if the data makes sense. If a card number isn't exactly 16 digits, we don't even bother the processor. This is handled by Pydantic for rock-solid data integrity.

The Banker (Decision Logic): * ✅ Approved: If the card is valid and the amount is reasonable.

⛔ Insufficient Funds: Try to charge more than 1,000€, and the system will pull the handbrake.

❌ Invalid Data: Clear error messages instead of cryptic crashes.

🛠️ Tech Stack (The "Why")
Python 3.10: My language of choice for its readability and power.

FastAPI: I chose this over Flask because I wanted high performance and, honestly, because the automatic Swagger documentation is a lifesaver for testing.

Pydantic: Essential for Fintech. When dealing with money, you can't afford to have a "string" where a number should be.

Uvicorn: The lightning-fast ASGI server that keeps everything running.

🚀 Take it for a spin
Want to try and "charge" yourself some virtual money?

Clone the repo:

Bash
git clone https://github.com/Anguis400/payment-gateway-api.git
cd payment-gateway-api
Install dependencies:

Bash
pip install fastapi uvicorn
Fire up the engine:

Bash
uvicorn main:app --reload
Interactive Testing: Head over to http://127.0.0.1:8000/docs. I've set up the Swagger UI so you can test POST requests directly from your browser without writing a single line of client-side code.

🧠 What I learned
Building this taught me that Backend development isn't just about moving data; it's about anticipating failure. Learning how to return the correct HTTP Status Codes (like 400 Bad Request vs. 402 Payment Required) is what separates a basic script from a professional API.

Built with ⌨️ and a lot of curiosity by Anguis400.