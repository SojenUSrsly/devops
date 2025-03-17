from flask import Flask

app - Flask(__name__)

@app.route("/")
def home():
	return "Hi, DevOps! It's work in conteiner!"

if __name__ == "__main__";
	app.run(host="0.0.0.0", port=5000)
