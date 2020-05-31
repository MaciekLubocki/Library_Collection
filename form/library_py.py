import os

from flask import Flask, render_template, request

UPLOAD_FOLDER = 'records'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/images/", methods=["GET", "POST"])
def form_view():
    if request.method == "POST":
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return "File is uploaded"
    return render_template('library.html')

if __name__ == '__main__':
    app.run(debug=True)