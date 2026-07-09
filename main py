# MIT License
# Copyright (c) 2024 Jayson
import http.client
import json
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("BLOCKCHAIN_API_KEY")

def check_btc_address(btc_address):
    if not API_KEY:
        print("ERROR: Walang API Key")
        return
    conn = http.client.HTTPSConnection("api.blockchain.info")
    headers = {'X-Explorer-Auth-Key': API_KEY}
    payload = json.dumps({"address": btc_address})
    conn.request("POST", "/explorer-gateway-kt/btc/address", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(json.dumps(json.loads(data), indent=2))
    conn.close()

if __name__ == "__main__":
    address = input("Ilagay BTC Address: ")
    check_btc_address(address)