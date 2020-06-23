from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')




@app.route('/', methods=['POST'])
def my_zc_post():
	print(request.form)
	phone_number = request.form['Phone number']
	airtime_amount = request.form['amount']
	airtime_topup(phone_number,airtime_amount)
	return phone_number + '/' + airtime_amount


def airtime_topup(phone_number, airtime_amount):
	# Import the Africa's Talking module here
	import africastalking

	#Define credentials here
	username = "wyclif"
	api_key = "6926a1e5a9ea9a25f1ca8"

	#Authenticate with the service
	africastalking.initialize(username, api_key)

	#Define the airtime service
	airtime = africastalking.Airtime 

	#Define user variables
	phone_number = phone_number
	amount = str(airtime_amount)
	currency_code = "KES"

	#Send the airtime!
	response = airtime.send(phone_number = phone_number, amount = airtime_amount, currency_code = currency_code)
	print(response)

if __name__ == '__main__':
    app.run(debug=True)
