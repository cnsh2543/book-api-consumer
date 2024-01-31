from flask import Flask, jsonify, request, render_template
import requests
import os 

app = Flask(__name__)

app.config['BOOK_API_URL'] = os.environ.get("BOOK_API_URL")


@app.route("/",  methods=["GET","POST"])
def index():
    if request.method == "POST":
        id = request.form.get("id")
        pub_year = request.form.get("pub_year")
        genre = request.form.get("genre")
        title = request.form.get("title")
        author = request.form.get("author")
                    
        

        book_url = app.config['BOOK_API_URL']
        params = {
            'id': id,
            'publication_year': pub_year,
            'genre': genre,
            'title': title,
            'author': author
        }

        records_data = requests.get(book_url, params=params).json()
    
        return render_template("records.html", books = records_data)
    else:
        return render_template("requests.html") 
    


