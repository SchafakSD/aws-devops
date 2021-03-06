from flask import Flask

app = Flask(__name__)

#decorators

@app.route("/")
def head():
    return "Hello World"


@app.route("/second")
def second():
    return "This is second page"


@app.route("/third/subthird")
def third():
    return"This is subthird page"


@app.route("/forth/<string:id>")
def forth(id):
    return f"Id of this page is {id}"


if __name__ == "__main__":
    app.run(debug = True) # lokalde debug modunda hazırladiktan sonra 80 portundan dis dunyaya yayinliyoruz.
    #app.run(host='0.0.0.0', port=80)