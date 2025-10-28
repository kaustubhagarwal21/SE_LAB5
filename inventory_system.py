import json
import logging
from datetime import datetime

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=None):
    if not item:
        return
    if logs is None:
        logs = []
    # basic type checks
    if not isinstance(item, str):
        print(f"Invalid item name (must be str): {item!r}")
        return
    try:
        qty = int(qty)
    except (TypeError, ValueError):
        print(f"Invalid qty (must be int): {qty!r}")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def removeItem(item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found; nothing to remove.")

def getQty(item):
    return stock_data.get(item, 0)

def loadData(file="inventory.json"):
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        # Start fresh if the file doesn't exist
        stock_data = {}
    except json.JSONDecodeError:
        print(f"Warning: '{file}' is not valid JSON. Starting with empty stock.")
        stock_data = {}

def saveData(file="inventory.json"):
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))

def printData():
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def checkLowItems(threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    addItem("apple", 10)
    addItem("banana", -2)
    addItem(123, "ten")  # invalid types, now safely handled
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()
    # eval("print('eval used')")  # dangerous
    print("Eval removed")

if __name__ == "__main__":
    # Optional: enable logging if you later switch prints to logging
    logging.basicConfig(level=logging.INFO)
    main()
