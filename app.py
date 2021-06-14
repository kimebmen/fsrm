from typing import final
from flask import Flask, render_template, request, redirect, url_for
import security as sec
import securityHome as secHome
from pathlib import Path
from waitress import serve

app = Flask(__name__)

@app.route('/')
def home():
    try:
        view_home = secHome.securityHome()
    except:
        view_home = "Not Found"

    return render_template("index.html", res=view_home, lengthh=len(view_home))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        try:
            keyword = request.form["search"]
            new_keyword = Path(keyword).resolve()
            f = open("C:\inetpub\wwwroot\Security_group_web\logs.txt", "w")
            f.write(f"new key: {str(new_keyword)}")
            f.close()
            final = sec.security(new_keyword)
        except:
            final = "Not Found"
    else:
        return redirect(url_for('home'))

    return render_template('result.html', folder=keyword, res=final, length=len(final))

@app.route('/detail', methods=['GET', 'POST'])
def detail():
    if request.method == "POST":
        try:
            keyword = request.form["direct"]
            print(keyword)
            new_keyword = Path(keyword).resolve()
            final = sec.security(new_keyword)
        except:
            final = "Not Found"
    else:
        return redirect(url_for('home'))

    return render_template('result.html', folder=keyword, res=final, length=len(final))

if __name__== '__main__':
    app.run(debug=False)
    # serve(app, host='0.0.0.0', port=5000, threads=1)
