import secrets
import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ValidationError
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import mysql.connector  # Import MySQL Connector
from typing import Optional
import logging

app = FastAPI()

mysql_config = {
    "host": "localhost",
    "user": "root",
    "password": "qwerty54321@",
    "database": "herbapp",
    "port": 3306,
}

conn = mysql.connector.connect(**mysql_config)
cursor = conn.cursor()

SECRET_KEY = secrets.token_urlsafe(64)
# Secret key for JWT

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# CORS Configuration
origins = [
    "http://localhost:8080",  # Update with your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.DEBUG)

# Log messages
logging.debug("Debug message")
logging.info("Information message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical error message")
# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

products = [
    {"id": 1, "name": "Basil", "price": 5.0, "image": "@/assets/Basil.png"},
    {"id": 2, "name": "Thyme", "price": 6.0, "image": "@/assets/Thyme.png"},
    {"id": 3, "name": "Chamomile", "price": 4.0, "image": "@/assets/Chamomile.png"},
    {"id": 4, "name": "Mint", "price": 3.0, "image": "@/assets/Mint.png"},
    {"id": 5, "name": "Lavender", "price": 7.0, "image": "@/assets/Lavender.png"},
]


class Products(BaseModel):
    id: int
    name: str
    price: float
    image: Optional[str] = None


class PaymentDetails(BaseModel):
    first_name: str
    last_name: str
    company_name: str
    address: str
    city: str
    postal_code: str
    phone: str


@app.post("/payment", response_model=PaymentDetails)
async def process_payment(payment_info: PaymentDetails):
    try:
        # Insert payment_info into the MySQL table
        insert_query = (
            "INSERT INTO payment (first_name, last_name, company_name, address, city, postal_code, phone) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        payment_data = (
            payment_info.first_name, payment_info.last_name, payment_info.company_name, payment_info.address,
            payment_info.city, payment_info.postal_code, payment_info.phone)
        cursor.execute(insert_query, payment_data)
        conn.commit()

        cursor.execute("SELECT * FROM payment_table WHERE id = LAST_INSERT_ID()")
        payment_info = cursor.fetchone()

        return {
            "id": payment_info[0],
            "first_name": payment_info[1],
            "last_name": payment_info[2],
            "company_name": payment_info[3],
            "address": payment_info[4],
            "city": payment_info[5],
            "postal_code": payment_info[6],
            "phone": payment_info[7],
        }



    except Exception as e:
        print("Error during payment processing:", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during payment processing",
        )


@app.get("/products", response_model=list[Products])
def get_products():
    return products


# Generate a JWT token for a user
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# User Model
class User(BaseModel):
    username: str
    password: str


class UserInDB(User):
    hashed_password: str


@app.post("/register", response_model=User)
async def register(user: User):
    try:

        hashed_password = pwd_context.hash(user.password)

        user_dict = user.dict()
        user_dict["hashed_password"] = hashed_password

        insert_query = "INSERT INTO user_table (username, hashed_password) VALUES (%s, %s)"
        user_data = (user.username, hashed_password)
        cursor.execute(insert_query, user_data)
        conn.commit()

        print("User registered successfully.")

        return user

    except ValidationError as e:
        # Handle validation errors here
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e),
        )

    except Exception as e:
        print("Error while registering user:", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while registering the user."
        )


@app.post("/login", response_model=dict)
async def login(user: User):
    try:
        # Retrieve user data from the MySQL table
        query = "SELECT username, hashed_password FROM user_table WHERE username = %s"
        cursor.execute(query, (user.username,))
        result = cursor.fetchone()

        if result is None or not pwd_context.verify(user.password, result[1]):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
            )

        # Generate JWT token
        user_data = {"sub": user.username}
        access_token = create_access_token(user_data)
        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        print("Error during login:", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during login."
        )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
