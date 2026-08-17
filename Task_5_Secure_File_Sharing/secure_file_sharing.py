from flask import Flask, request, send_file, render_template_string
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

UPLOAD_FOLDER = "secure_files"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


HTML = """
<h2>Secure File Sharing System</h2>

<form method="POST" action="/upload" enctype="multipart/form-data">
<input type="file" name="file">
<button type="submit">Upload & Encrypt</button>
</form>

<h3>Download File</h3>
<form method="POST" action="/download">
<input type="text" name="filename" placeholder="Enter filename">
<button type="submit">Download</button>
</form>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    data = file.read()

    encrypted_data = cipher.encrypt(data)

    path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(path, "wb") as f:
        f.write(encrypted_data)

    return "File uploaded and encrypted successfully!"


@app.route("/download", methods=["POST"])
def download():

    filename = request.form["filename"]

    path = os.path.join(UPLOAD_FOLDER, filename)

    if os.path.exists(path):

        with open(path, "rb") as f:
            encrypted_data = f.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        output = "decrypted_" + filename

        with open(output, "wb") as f:
            f.write(decrypted_data)

        return send_file(output, as_attachment=True)

    return "File not found"


if __name__ == "__main__":
    app.run(debug=True)