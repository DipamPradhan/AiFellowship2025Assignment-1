import os

from dotenv import load_dotenv
import uvicorn

load_dotenv()

host = os.getenv("APP_HOST", "0.0.0.0")
port = int(os.getenv("APP_PORT", "5000"))

if __name__ == "__main__":
    uvicorn.run("moviefinder.app:app", host=host, port=port)
