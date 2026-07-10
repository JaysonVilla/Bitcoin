https://api.blockchain.info/explorer-gateway-kt

Optional. Send your Explorer API key in the X-Explorer-Auth-Key header. Requests sent without a key fall back to the default rate limits.
Name
:
X-Explorer-Auth-Key
Value
:
Client Libraries
Python http.client
# Build and Release Folders
bin-debug/
bin-release/
[Oo]bj/
[Bb]in/

# Other files and folders
.settings/

# Executables
*.swf
*.air
*.ipa
*.apk

# Project files, i.e. `.project`, `.actionScriptProperties` and `.flexProperties`
# should NOT be excluded as they contain compiler settings and other important
# information for Eclipse / Flash Builder.
MIT License

Copyright (c) 2024 Jayson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
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