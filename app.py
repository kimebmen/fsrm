from typing import final
from flask import Flask, render_template, request, redirect, url_for
import fs01 as fs01
import fs01Home as fs01Home
import fs02 as fs02
import fs02Home as fs02Home
import fs03 as fs03
import fs03Home as fs03Home
import fsx as fsx
import fsxHome as fsxHome
import archive as archive
import archiveHome as archiveHome
from pathlib import Path
from waitress import serve

app = Flask(__name__)

# @app.route('/')
# def home():
#     try:
#         view_home = kpcsgtHome.kpcsgtHome()
#     except:
#         view_home = "Not Found"

#     return render_template("index.html", res=view_home, lengthh=len(view_home))

@app.route('/')
def home():
    return render_template("menu.html")

# fs03
@app.route('/fs03')
def homefs03():
    try:
        view_home = fs03Home.fs03Home()
    except:
        view_home = "Not Found"

    return render_template("indexfs03.html", res=view_home, lengthh=len(view_home))

@app.route('/detailfs03', methods=['GET', 'POST'])
def detailfs03():
    if request.method == "POST":
        try:
            keyword = request.form["direct"]
            print(keyword)
            new_keyword = Path(keyword).resolve()
            final = fs03.fs03(new_keyword)
        except:
            final = "Not Found"
    else:
        return redirect(url_for('homefs03'))

    return render_template('resultfs03.html', folder=keyword, res=final, length=len(final))

# fs01
@app.route('/fs01')
def homefs01():
    try:
        view_home = fs01Home.fs01Home()
    except:
        view_home = "Not Found"

    return render_template("indexfs01.html", res=view_home, lengthh=len(view_home))

@app.route('/detailfs01', methods=['GET', 'POST'])
def detailfs01():
    if request.method == "POST":
        try:
            keyword = request.form["direct"]
            print(keyword)
            new_keyword = Path(keyword).resolve()
            final = fs01.fs01(new_keyword)
        except:
            final = "Not Found"
    else:
        return redirect(url_for('homefs01'))

    return render_template('resultfs01.html', folder=keyword, res=final, length=len(final))

# fs02
@app.route('/fs02')
def homefs02():
    try:
        view_home = fs02Home.fs02Home()
    except:
        view_home = "Not Found"

    return render_template("indexfs02.html", res=view_home, lengthh=len(view_home))

@app.route('/detailfs02', methods=['GET', 'POST'])
def detailfs02():
    if request.method == "POST":
        try:
            keyword = request.form["direct"]
            print(keyword)
            new_keyword = Path(keyword).resolve()
            final = fs02.fs02(new_keyword)
        except:
            final = "Not Found"
    else:
        return redirect(url_for('homefs02'))

    return render_template('resultfs02.html', folder=keyword, res=final, length=len(final))

# fsx
@app.route('/fsx')
def homefsx():
    try:
        view_home = fsxHome.fsxHome()
    except:
        view_home = "Not Found"

    return render_template("indexfsx.html", res=view_home, lengthh=len(view_home))

@app.route('/detailfsx', methods=['GET', 'POST'])
def detailfsx():
    if request.method == "POST":
        try:
            keyword = request.form["direct"]
            print(keyword)
            new_keyword = Path(keyword).resolve()
            final = fsx.fsx(new_keyword)
        except:
            final = "Not Found"
    else:
        return redirect(url_for('homefsx'))

    return render_template('resultfsx.html', folder=keyword, res=final, length=len(final))

# archive
@app.route('/archive')
def homearchive():
    try:
        view_home = archiveHome.archiveHome()
    except:
        view_home = "Not Found"

    return render_template("indexarchive.html", res=view_home, lengthh=len(view_home))

@app.route('/detailarchive', methods=['GET', 'POST'])
def detailarchive():
    if request.method == "POST":
        try:
            keyword = request.form["direct"]
            print(keyword)
            new_keyword = Path(keyword).resolve()
            final = archive.archive(new_keyword)
        except:
            final = "Not Found"
    else:
        return redirect(url_for('homearchive'))

    return render_template('resultarchive.html', folder=keyword, res=final, length=len(final))


if __name__== '__main__':
    # app.run(debug=False)
    serve(app, host='0.0.0.0', port=5000, threads=1)
