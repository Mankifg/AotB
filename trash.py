'''
if not hold["auctionInfo"]["buyPrice"] == None:
        price = hold["auctionInfo"]["buyPrice"]
    else:
        if not hold["bazaarInfo"]["buyPrice"] == None:
            price = hold["bazaarInfo"]["buyPrice"]
        else:
            print(f'[ALERT]Price for {item} not found. ')
'''