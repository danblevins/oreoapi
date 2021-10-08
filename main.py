from flask import Flask, render_template, jsonify, send_file
from utils.randomize_image import randomize_image
from utils.read_config import read_config

app = Flask(__name__)
config = read_config()
app.config.update(config)

### Web Pages ###
@app.route("/")
def home():
    return render_template("index.html", config=config)

@app.route("/cookiejar")
def cookiejar():
    image = randomize_image()
    filename, file_extension = image.split(".")
    mimetype = "image/" + file_extension

    return send_file(config["images"] + image, mimetype=mimetype)

@app.route("/cookiejar.json")
def cookiejar_json():
    image = randomize_image()

    return jsonify({
        "oreo": "www.test.com/" + image
        })

@app.errorhandler(404)
def page_not_found(e):
    return ('Uh Oh Oreo! 404 Page Not Found'), 404

if __name__ == '__main__':
    app.run()