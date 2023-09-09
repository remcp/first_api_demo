from flask import Flask, jsonify, request
from selenium_test import getprices
import requests

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def retrieve_data():
    search = request.args.get('search')
    data = getprices(search)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
    
