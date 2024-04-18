from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/prediction', methods = ['POST'])
def predict():
    if request.method == 'POST':
        Age = float(request.form['Age'])
        Annual_Income = float(request.form['Annual_Income'])
        Num_of_Delayed_Payment = float(request.form['Num_of_Delayed_Payment'])
        Num_Bank_Accounts = float(request.form['Total_Num_Credit_Products'])
        Outstanding_Debt = float(request.form['Outstanding_Debt'])

        features = [[Age , Annual_Income , Num_of_Delayed_Payment , Num_Bank_Accounts ,Outstanding_Debt]]
        print(features)
        model = pickle.load(open('model_dtc.pkl', 'rb'))
            
        prediction = model.predict(features)
        print(prediction)
        
        mapping = {0: 'GOOD', 1: 'POOR', 2: 'STANDARD'}
        predicted_result = mapping[prediction[0]]
        print(predicted_result)

    return render_template("prediction.html", result=predicted_result)


if __name__ == '__main__':
    app.run()