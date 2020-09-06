# alttaki belgeyi olustur, github repona "git add ." ve "git commit -m 'deneme'" ve "git push" ile github repona gonder
# github repondan wget ile EC2 instance a cek, run et ve ardindan connection to webpage

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80) #80 portundan herhangi bir adresten gelen istegi calistirir 