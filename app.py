from flask import Flask

# __name__ = "__main__"
app = Flask(__name__)

@app.route("/first")
def hello_world():
    return "Hello World"

@app.route("/about")
def sobre():
    return "Pagina sobre"

# Somente para ambiente de desenvolvimento
if __name__ == "__main__":
    app.run(debug=True)