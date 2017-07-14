from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
     return render_template("index.html")


@app.route('/whereami')

def whereami():
     return "Kdua"
if __name__ == '__main__':
         app.run(host="0.0.0.0")


@app.rout(name)
def send_from(name):
     return send_fcdrom_directory("index.thml",name)
