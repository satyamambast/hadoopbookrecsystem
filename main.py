from flask import Flask, render_template,request
import os
import nltk,string
stemmer = nltk.stem.SnowballStemmer("english")
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

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
        result = request.form
        words=result["Name"].split(",")
        words=[stemmer.stem(words.lower().translate(string.punctuation)) for words in words]
        words=[words.strip() for words in words]
        cmd="./runexperiment.sh "+",".join(words)
        os.system(cmd)
        with open("top5books.txt","r") as t5:
            revelist=t5.readlines()
        revelio={}
        for i in range(5):
            bookrel=revelist[i].split(":sep:")
            revelio["t"+str(i)]=bookrel[0].title()
            revelio["a"+str(i)]=bookrel[1].title()
            revelio["r"+str(i)]=bookrel[2]
        # for i in revelio:
        #     print(i,revelio[i])


        #return render_template("result.html",result = result)
        return render_template("show_results.html",revelio=revelio)

    
if __name__ == "__main__":
    app.run(debug=True)