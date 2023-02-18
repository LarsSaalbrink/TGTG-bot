


#####Imports#####
from enum import Enum

#####Classes#####
"""
class BagType(Enum):
  FRUGT_OG_GRONT: 1
  KOD_OG_KOL: 2
  BAGER: 3
  DAGLIGVARER: 4
  FROST: 5
"""

BagType = Enum('Color', ['FRUGT_OG_GRONT', 'KOD_OG_KOL', 'BAGER', 'DAGLIGVARER', 'FROST'])

class Bag:
    def __init__(self, type, price, releaseTime, pickupTimespan):
        self.type = type  #BagType(Enum)
        self.price = price
        self.releaseTime = releaseTime
        self.pickupTimespan = pickupTimespan

        #Read from file if entry exists, else set to 0 and
        #create entry in file
        self.orderCountHistory = 0

class Shop:
    def __init__(self, chainName, bagsAvailable, distanceFromHome):
        self.chainName = chainName
        self.bagsAvailable = bagsAvailable   #Bag class
        self.distanceFromHome = distanceFromHome