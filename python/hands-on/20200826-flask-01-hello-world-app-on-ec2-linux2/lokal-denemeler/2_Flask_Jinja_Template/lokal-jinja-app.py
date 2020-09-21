from flask import Flask, render_template #html sayfasini dondurebilmek icin render_template ekledik


app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1 = 12) 
    #render_template yardimiyla index.html sayfasina gidiyor
    #app.py de tanimladigimiz bir number1 degiskenini index.html de {{number1}} seklinde gosteriyoruz.

@app.route("/ikinci")
def second():
    return render_template("yeni.html", hazirlayan = "Ahmet") 
    #render_template yardimiyla yeni.html sayfasina gidiyor
    #app.py de tanimladigimiz bir hazirlayan degiskenini index.html de {{hazirlayan}} seklinde gosteriyoruz.

if __name__ == "__main__":
    app.run(debug = True) 