
from flask import Flask,render_template,request
from Model.utils import iris
import config

app=Flask(__name__)
@app.route('/')
def sms ():
    return render_template("index.html")

@app.route('/api',methods=["POST"])
def result():
    Input=request.form.get
    SepalLengthCm=eval(Input('SepalLengthCm'))
    SepalWidthCm=eval(Input('SepalWidthCm'))
    PetalLengthCm=eval(Input('PetalLengthCm'))
    PetalWidthCm=eval(Input('PetalWidthCm'))

    abc=iris(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
    abs=abc.prediction()

    return render_template("index.html",pred=abs[0])
if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER)



