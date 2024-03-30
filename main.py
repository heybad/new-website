from flask import Flask, render_template

app = Flask(__name__)

# Define the GitHub URL
github = 'https://github.com/kmohamud10/List-of-largest-companies'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project1', methods=['GET', 'POST'])
def agevsincome():
    # Assuming project1.agevsincome() returns some data to render
    return project1.agevsincome()

@app.route('/project2')
def project2():
    # Pass the github_url variable to the template
    return render_template('project2.html', github =github)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
