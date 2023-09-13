import sys
import requests
import json

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

qty = sys.argv[1]

try:
    qty = float(qty)

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

try:
    valueJson = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    value = valueJson.json()
    # print(json.dumps(value, indent=4))

    usd_value = value["bpi"]["USD"]["rate_float"]
    usd_value = float(usd_value)

    usd_value_total = usd_value * qty

    print(f"${usd_value_total:,}")

except requests.RequestException:
    pass