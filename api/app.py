from flask import Flask, jsonify, request, render_template
import requests
import os 

app = Flask(__name__)


# Get app's secret key so Flask_login can manipulate the session
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

        # attempt the API call, and rename empty strings
        # for both or either fields if not available
        
        records_data = requests.get(book_url, params=params).json()
        # records_data = requests.get("http://book-api-server-mw-cn.gughggamejekg9cb.uksouth.azurecontainer.io?id=1")
        print(records_data)
        return render_template("records.html", books = records_data)
    else:
        return render_template("requests.html") 
    


