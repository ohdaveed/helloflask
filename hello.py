from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv() # Load environment variables from .env file


@app.route("/")
def home():
    return "Hello World! I'm using Flask."