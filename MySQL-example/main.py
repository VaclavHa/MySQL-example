
from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route("/", methods=['GET'])
def get_invoice():
    pass


@app.route("/add", methods=['POST'])
def add_invoice():
    pass



@app.route("/delete", methods=['POST'])
def delete_invoice():
    pass

if __name__ == '__main__':
    app.run(debug=True)