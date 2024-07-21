from flask import Flask, request, render_template
import pyshorteners

app = Flask(__name__) 

@app.route("/", methods = ["GET", "POST"])
def index():
    print(request.form)
    if request.method == "GET":     
        return render_template('index.html')
    else:
        url = request.form.get("url")
        new_url = pyshorteners.Shortener()
        shortened_url = new_url.tinyurl.short(url)
        context = {
            'url'      : url,
            'url_nueva'   : shortened_url,
        }
        return render_template('index.html', **context)


app.run(host='0.0.0.0',  port=3000,  debug=True)