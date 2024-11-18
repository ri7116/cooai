from flask import Flask, jsonify, request

app = Flask(__name__)

# 샘플 데이터
items = ["1234","123"]

# GET: 데이터 가져오기
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# POST: 데이터 추가
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    items.append(data)
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
