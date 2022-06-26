
import requests
import json
from requests.models import requote_uri
from data import data
import json
import os
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
}"""}).json()

print(itemSbq)
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