from flask import Flask, render_template, redirect, url_for, session, request
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

drive_train_order = ['Front', 'All', 'Rear']

label_encoder = LabelEncoder()
ordinal_encoder = OrdinalEncoder(categories=[drive_train_order])

app = Flask(__name__)
app.secret_key = 'zaid'

with open('car_price_prediction.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input_features', methods=['POST', 'GET'])
def input(): 
    if request.method == 'POST':
        session['Make'] = request.form.get('Make')
        session['Type'] = request.form.get('Type')
        session['Origin'] = request.form.get('Origin')
        session['DriveTrain'] = request.form.get('DriveTrain')
        session['MSRP'] = float(request.form.get('MSRP'))
        session['EngineSize'] = float(request.form.get('EngineSize'))
        session['Cylinders'] = int(request.form.get('Cylinders'))
        session['Horsepower'] = float(request.form.get('Horsepower'))
        session['Weight'] = float(request.form.get('Weight'))
        session['Wheelbase'] = float(request.form.get('Wheelbase'))
        session['Length'] = float(request.form.get('Length'))
        return redirect(url_for('result'))
    return render_template('input_features.html')

@app.route('/result')
def result():
    input_data = pd.DataFrame({
        'Make': [session.get('Make')],
        'Type': [session.get('Type')],
        'Origin': [session.get('Origin')],
        'DriveTrain': [session.get('DriveTrain')],
        'MSRP': [session['MSRP']],
        'EngineSize': [session['EngineSize']],
        'Cylinders': [session['Cylinders']],
        'Horsepower': [session['Horsepower']],
        'Weight': [session['Weight']],
        'Wheelbase': [session['Wheelbase']],
        'Length': [session['Length']]
    })

    input_data['Make'] = label_encoder.fit_transform(input_data['Make'])
    input_data['Type'] = label_encoder.fit_transform(input_data['Type'])
    input_data['Origin'] = label_encoder.fit_transform(input_data['Origin'])

    input_data['DriveTrain'] = ordinal_encoder.fit_transform(input_data[['DriveTrain']])

    prediction = model.predict(input_data)

    predicted_price = round(prediction[0], 2)

    return render_template('result.html', price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
