from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home_page.html")
    
@app.route("/about")
def about():
    return render_template("web_1920___1.html")
    
@app.route("/search")
def search():
    return render_template("search_page_1.html")

@app.route("/results")
def results():
    return render_template("show_results.html")

    
if __name__ == "__main__":
    app.run(debug=True)