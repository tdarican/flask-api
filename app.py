from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'API çalışıyor!'

@app.route('/merhaba')
def merhaba():
    isim = request.args.get('isim', 'dünya')
    return jsonify({'mesaj': f'Merhaba, {isim}!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
