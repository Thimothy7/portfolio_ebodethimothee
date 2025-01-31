from flask import Flask, render_template, url_for, request, redirect
import csv
import sys

# Create a Flask app instance
app = Flask(__name__)
print(__name__)

# Define a route and view function
@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        name= data["name"]
        message= data["message"]
        file = database.write(f'\n{email},{name},{message}')

def write_to_csv(data):
    with open('database.csv', newline="", mode='a') as database2:
        email = data["email"]
        name= data["name"]
        message= data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,name,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
       return 'something went wrong. Try aigain!' 
            

# Run the app if this file is executed
if __name__ == '__main__':
    app.run(debug=True)
