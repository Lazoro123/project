import os
from passlib.context import CryptContext
from jose import jwt

SECRET_KEY = os.getenv("SECRET_KEY", "change_this")
ALGORITHM = "HS256"
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(p): return pwd.hash(p)
def verify_password(plain, hashed): return pwd.verify(plain, hashed)
def create_token(data: dict): return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
