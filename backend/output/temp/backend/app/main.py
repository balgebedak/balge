from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
#import firebase_admin
#from firebase_admin import credentials, auth
#import stripe

# Initialize Firebase Admin SDK
#cred = credentials.Certificate("path/to/your/firebase/credentials.json")
#firebase_admin.initialize_app(cred)

# Initialize Stripe
#stripe.api_key = "your_stripe_secret_key"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    email: str
    password: str

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float

class Order(BaseModel):
    items: List[Item]
    total: float

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        #user = auth.get_user_by_email(form_data.username)
        # Validate password here (implement your own logic)
        return
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid credentials")

@app.get("/items/", response_model=List[Item])
async def read_items():
    return [
        Item(id=1, name="Pizza", description="Delicious cheese pizza", price=9.99),
        Item(id=2, name="Burger", description="Juicy beef burger", price=5.99),
    ]

@app.post("/order/")
async def create_order(order: Order, token: str = Depends(oauth2_scheme)):
    #try:
        # Verify the token
        #decoded_token = auth.verify_id_token(token)
        #user_id = decoded_token['uid']

        # Create a Stripe charge
        #stripe.Charge.create(
         #   amount=int(order.total * 100),  # amount in cents
         #   currency="usd",
          #  description="Food Delivery Order",
           # source=token  # Use a valid source token from the frontend
        #)

        #return {"status": "Order placed successfully", "user_id": user_id}
    #except Exception as e:
     #   raise HTTPException(status_code=400, detail=str(e))