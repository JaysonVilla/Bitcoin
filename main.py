# loaded. Ready t
    
    conn.request("POST", "/explorer-gateway-kt/btc/address", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(json.dumps(json.loads(data), indent=2))

if __name__ == "__main__":
    address = input("Ilagay BTC Address: ")
    check_btc_address(address)