from flask import Flask, render_template, request, redirect, url_for, jsonify
import glob
app = Flask(__name__,static_url_path='/')

import data
app.register_blueprint(data.app)

@app.route('/')
def index():
	l=sorted(glob.glob("data/*.txt"))
	return render_template('index.html',message=l)

# /post にアクセスしたときの処理
@app.route('/list', methods=['GET'])
def get_list():
	l=glob.glob("data/*.txt")
	return jsonify(ResultSet=l)

if __name__ == '__main__':
	#app.debug = True
	app.run(host='0.0.0.0')
