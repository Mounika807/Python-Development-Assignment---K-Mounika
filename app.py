from flask import Flask, render_template, request
app = Flask(__name__, template_folder='E:/projecttt')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        # Here you can perform any action with the form data,
        # such as saving it to a database, sending an email, etc.
        # For example, let's just print the data for demonstration:
        print("Name:", name)
        print("Email:", email)
        
        # You can redirect to a thank you page or display a message here
        return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
