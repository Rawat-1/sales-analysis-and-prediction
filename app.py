from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")  #this is called routing, it is used to map the URL to a function, going to different pages of the website such as login, signup,etc. Also "/" means the homepage of the website.


def home():
    return render_template("index.html")  #this is will return the index file as homepage and display the HTML file in the browser.

@app.route("/analytics")
def analytics():
    return render_template("analytics.html")  #this is will return the analytics file and display the HTML file in the browser.



if __name__ == '__main__':
    app.run(debug="True")  #this will run the app in debug mode, which means that if there is any error in the code, it will show the error in the browser.