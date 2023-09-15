keepPlaying = True
auctionBids = {}
keepPlayingInput = ''
while keepPlaying:
    name = input("What is your name?")
    bid = input("What is your bid?")
    auctionBids[name] = bid
    keepPlayingInput = input("Would you like to bid again?(y/n)").lower()
    if keepPlayingInput == "n":
        keepPlaying = False

Keymax = max(zip(auctionBids.values(), auctionBids.keys()))[1]
print(f"The highest bid is {auctionBids[Keymax]} and belongs to {Keymax}")


