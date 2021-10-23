from flask import Flask, send_file,request,url_for
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "HOME"
@app.route("/<fname>/")
def fileshow(fname):
    if request.method == "GET":
        url = fname
        url_path = str(url)
        if os.path.exists(f"static/{url_path}"):
            response = send_file("static/"+url_path,as_attachment=True)
            return (response),200
        else:
            return ("Package Not Found"),404
    return response

if __name__ == "__main__":
    app.run(debug=True)

