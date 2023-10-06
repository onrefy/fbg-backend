from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/calculate', methods=['POST'])
def calculate():
    # 在此处执行后端计算
    data = {"result": "Backend calculation result"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
