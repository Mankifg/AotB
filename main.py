import requests
import json
from requests.models import requote_uri
from data import data
import json
import os
from dotenv import load_dotenv
load_dotenv()

print("[START] Program started")

key = os.getenv("TYPE")
if key == None:
    key = ''


PATH = "items/"
ALPHABET = ["A1", "A2", "A3", "B1", "B2", "B3","C1","C2","C3"]







print("[START] Program ready")

HYPIXEL_LINK = "https://api.hypixel.net/skyblock/bazaar"
LOWESTBIN_LINK = "https://moulberry.codes/lowestbin.json"
SBQ_LINK = "https://sbquery.ml/"

lbin = requests.get(LOWESTBIN_LINK).json()
print("[API] Lbins get")

hypixel = requests.get(HYPIXEL_LINK).json()["products"]
print("[API] Hypixel api get")

itemSbq = requests.post(SBQ_LINK, json={"query": """
{
  sbItems {
    name
    itemId
    neuInfo {
      recipe
    }
    auctionInfo {
      buyPrice
    }
    bazaarInfo {
      buyPrice
      sellPrice
    }
  }
}"""}).json()["data"]["sbItems"]

everyItem = requests.post(SBQ_LINK, json={"query": """
{
  sbItems {
    name
  }
}"""}).json()["data"]["sbItems"]

everyItem = [item["name"] for item in everyItem]

#print(lbin)

itemSbq = {item["itemId"]: item for item in itemSbq}

print("[API] SBQ api get")


def make_short(price):
     if price > 1000000:
        new_price = price / 1000000
        new_price = str(new_price) + 'm'
     elif price > 1000:
        new_price = price / 1000
        new_price = str(new_price) + 'k'
     return new_price

def make_readable(item):
    item = item.upper()
    item = item.replace(" ", "_")
    item = itemSbq[item]

    return item

def make_nice(item):
    item.upper()
    item = item.title()
    item = item.replace("_", " ")
    return item

def get_price(item):
    item = make_readable(item)
    
    try:
        price = int(hypixel[item]["quick_status"]["buyPrice"])
    except KeyError:
        try:
            price = int(lbin[item])
        except KeyError:
            
            price = getRecipePrice(item)
    print(item)
    return price


def getRecipe(item):
    item = make_readable(item)
    return itemSbq[item]["neuInfo"]["recipe"]

def getRecipePrice(item):
    print("Item id:" + itemSbq[make_readable(recipe)]["itemId"])
    #recipe = getRecipe(itemSbq[make_readable(recipe)]["itemId"])
    recipe = getRecipe(item)
    
    wholePrice = 0
    
    for c in range(len(recipe)):
        
        hold = recipe[c]
        if not hold == "":
            h2 = hold.split(":")
            
            item = h2[0]
            amount = int(h2[1])
            itemPrice = get_price(item)
            wholePrice += amount * itemPrice
    return wholePrice

print("[INFO] Functions load")

big_items = []
small_items = []
diff = []

ench_items = []

for i in range(len(everyItem)):
    if "Enchanted" in everyItem[i]:
        ench_items.append(everyItem[i])
        
for i in range(len(ench_items)):
    print(f"{ench_items[i]} | {get_price(ench_items[i]) - getRecipePrice(ench_items[i])}")
