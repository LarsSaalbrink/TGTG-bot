# Next up:
"""
-Lav function der
    *Læser OdenseShops dictionary
    *Udpakker den abstrakte klassedata
    *Genindpakker dataen son json objekter (?)
    *Sender json objekter til frontend

-Find en HTML struktur der kan displaye dynamisk ud fra interaktion med javascript

-Implementer javascript der kan interagere med HTML elementet for at tilføje de modtagede json objekter
"""


#Architecture consideration:
"""
-Keep functionality blocks small and easily testable

-Be vigilant about spaghetti, you may want to expand this for use by multiple
  people later

-Try to stick to website building theory (fronend, transport layer, backend)

-Make a failsafe way to pull the plug to prevent rampant ordering 
 (shut down script button?)
"""

#Todo list:
"""
-Class for bag
  *Tracker of how many times you have ordered this bag
    (Save this in a file)

-Online website with interface to script
  *List of all bags (which have been manually added to the script)
  *Buttons to add bag to order
  *Date when you want the bags
  *Buttons to confirm and cancel order
  *List of current orders, date for which they have been ordered, and individual
   pickup times

-Text on image recognizer that can search for a given bag address 
 (including scrolling) and return screen coordinates & scroll distance
 for where to click to order the bag

-Autoclick functionality based on custom type containing the screen coordinates

-Ordering function
  *Looks at amount of bags ordered through website
  *Reads payment details from file (to keep it hidden from copilot)
  *Inputs the payment details and confirms the order
  *Returns if the order was successful or not

"""

#Strecth goal todo:
"""
-Add interface to google maps to find the distance from home to the shop
"""




from lib.shops import Shop, Bag, BagType
from lib.web import app
import warnings

def main():
    print('Mojn')
    warnings.warn('\nWarning...........orderCountHistory of Bag class not in use\n')

    ###Init###
    odenseShops = {}  #Dictionary of shops in Odense (string/Shop)
    #instantiating shops

    #Missing release date of bager bag
    warnings.warn('\nWarning...........Missing release date of bager bag for Føtex Middelfartvej 125\n')
    odenseShops['Middelfartvej 125'] = Shop('Føtex', 
                                            [Bag(BagType.FRUGT_OG_GRONT.name,29,'21:00','19:00 - 20:00'),
                                             Bag(BagType.BAGER.name,29,'23:59','19:00 - 20:00')], 
                                            0.9)  

    odenseShops['Bystævnevej 3'] = Shop('Lidl', 
                                        [Bag(BagType.FRUGT_OG_GRONT.name,29,'13:20','19:00 - 20:00'),
                                         Bag(BagType.KOD_OG_KOL.name,29,'13:20','9:00 - 13:00')],
                                        0.9)


    app.run()

    ###Loop###
    #while(1):
      #Do something

#####Main#####
if __name__ == "__main__":
    main()