from flask import Flask
from random import randint

app = Flask(__name__)
img1_URL= ""

def make_bold(func):
    def wrapper(*args, **kwargs):
        final_text= "<b>"+ str(func()) + "</b>"
        return final_text
    return wrapper

@app.route("/")
def hello_world():
    return "<h2> guess a number from 0 to 10 </h2>"

@app.route("/bye")
@make_bold
def bye():
    return "BYE!"

# choice_num= randint(0,10)

@app.route("/<int:number>")
def guesser(number):
    if number == choice_num:
        print('you got it')
if __name__ == "__main__":
    app.run(debug=True)

print("this is second push commit 2")