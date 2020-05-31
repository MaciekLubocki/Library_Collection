import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)


@app.route('/library.html', methods=['GET'])
def message_my_page():
    print("I am written to the file")
    return render_template("/library.html")
if __name__ == '__main__':
    app.run()

UPLOAD_FOLDER = 'records'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/images/", methods=["GET", "POST"])
def form_view():
    if request.method == "POST":
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return "File is uploaded"
    return render_template('parent.html')

if __name__ == '__main__':
    app.run(debug=True)



