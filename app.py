from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bio_form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        hobbies_input = request.form.get('hobbies', '')
        hobbies = [h.strip() for h in hobbies_input.split(',') if h.strip()]
        return render_template('bio_card.html', name=name, age=age, hobbies=hobbies)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
