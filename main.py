# MIT License
# Copyright (c) 2024 Jayson
import http.client, json, os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("BLOCKCHAIN_API_KEY")
print("API Key loaded. Ready to check BTC")