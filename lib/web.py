from flask import Flask, render_template
import jyserver.Flask as jsf

app = Flask(__name__)

@jsf.use(app)
class App:
    # def __init__(self):
    #     self.count = 0

    calls = 0

    def alertTest(self, callername):
        print('Called by: ', callername)

        App.calls += 1
        self.js.document.write(App.calls)


@app.route('/')
def hello_world():
    return App.render(render_template('index.html'))