from flask import Flask, render_template, request, send_file
import cv2
from steganography import encode, decode
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encode", methods=["GET", "POST"])
def encode_image():
    if request.method == "POST":
        file = request.files["image"]
        message = request.form["message"]

        file.save("input.png")

        img = cv2.imread("input.png")
        encoded = encode(img, message)

        cv2.imwrite("output.png", encoded)

        return send_file("output.png", as_attachment=True)

    return render_template("encode.html")

@app.route("/decode", methods=["GET", "POST"])
def decode_image():
    if request.method == "POST":
        file = request.files["image"]
        file.save("encoded.png")

        img = cv2.imread("encoded.png")
        message = decode(img)

        return render_template("result.html", message=message)

    return render_template("decode.html")
if __name__ == "__main__":
    app.run(debug=True)  