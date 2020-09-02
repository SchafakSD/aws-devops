from flask import Flask


app = Flask(__name__)


if __name__ == "__main__": # dogru yerde calisiyormuyuz diye kontrol ediyoruz.
    app.run(debug = True) # lokalde debug modunda hazırladiktan sonra 80 portundan dis dunyaya yayinliyoruz.