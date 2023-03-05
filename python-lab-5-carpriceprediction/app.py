from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))  # loading the trained model


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# In the above code, are returning the output of the function "render_template()".
# This function accepts an input of an HTML page.
# This function looks for the mentioned page under templates folder.
# This is the reason we created this index.html form under templates folder.



# Predict function to read the values from the UI and predict the price value.
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age_of_the_car = request.form['age_of_the_car']
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Fuel_Type = request.form['Fuel_Type']
        Seller_Type = request.form['Seller_Type']
        Transmission = request.form['Transmission']
        Owner = request.form['Owner']

        prediction = model.predict([[age_of_the_car, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner]])
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text='Selling price of car is {} lakhs'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True