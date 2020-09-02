from flask import Flask, render_template #html sayfasini dondurebilmek icin render_template ekledik


app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1 = 12) 
    #render_template yardimiyla index.html sayfasina dön
    #app.py de tanimladigimiz bir degiskeni index.html de {{degisken}} seklinde gosterebiliyoruz.

@app.route("/ikinci")
def second():
    return render_template("yeni.html", hazirlayan = "Ahmet") 



if __name__ == "__main__":
    app.run(debug = True) 