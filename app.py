from flask import Flask

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "I have made these changes in the app.py"

if __name__=="__main__":
    app.run(debug=True)