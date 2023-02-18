from flask import Flask, render_template
import jyserver.Flask as jsf

app = Flask(__name__)

@jsf.use(app)
class App:
    # def __init__(self):
    #     self.count = 0

    odenseShops = {}

    def alertTest(self, callername):
        print('Called by: ', callername)

        App.calls += 1
        self.js.document.write(App.calls)

    def addShop(self, shopAdr):
        shopObj = App.odenseShops[shopAdr]
        table = self.js.document.getElementById("mainT")

        row = table.insertRow(-1)

        #print('Adding following shop:\n')
        #print('Chain name: ', shopObj.chainName)
        row.insertCell(-1).innerHTML = shopObj.chainName
        #print('Distance from home: ', shopObj.distanceFromHome)
        row.insertCell(-1).innerHTML = shopObj.distanceFromHome
        #print('Bags available: ')


        # GOT TO HERE----------------------------------------------------------


        # for bag in shopObj.bagsAvailable:
        #     #print('---\nBag type: ', bag.type)
        #     row.insertCell(-1).innerHTML = bag.type
        #     #print('Bag price: ', bag.price)
        #     row.insertCell(-1).innerHTML = bag.price
        #     #print('Bag release time: ', bag.releaseTime)
        #     row.insertCell(-1).innerHTML = bag.releaseTime
        #     #print('Bag pickup timespan: ', bag.pickupTimespan)
        #     row.insertCell(-1).innerHTML = bag.pickupTimespan

        #     row = table.insertRow()
              
@app.route('/')
def hello_world():
    return App.render(render_template('bs_test.html'))