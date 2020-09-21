# alttaki belgeyi olustur, github repona "git add ." ve "git commit -m 'deneme'" ve "git push" ile github repona gonder
# github repondan wget ile EC2 instance a cek, run et ve ardindan connection to webpage

# Import Flask modules
from flask import Flask

# Create an object named app 
app = Flask(__name__)

# Create a function `hello` which returns a string `Hello World`, and
# Assign a URL route the `hello` function with decorator `@app.route('/')`.
@app.route("/")
def hello():
    return "Hello World!"

# Enable the web application to be run in main, so that it can be reached from anywhere from port 80.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80) #80 portundan herhangi bir adresten gelen istegi calistirir 