from flask import Flask, render_template

app = Flask(__name__)

# Variable to store the number of clicks
click_count = 0

@app.route('/')
def index():
    return render_template('index.html', click_count=click_count)

@app.route('/click', methods=['POST'])
def click():
    global click_count
    click_count += 1
    return render_template('index.html', click_count=click_count)

@app.route('/change_color', methods=['POST'])
def change_color():
    global click_count
    if click_count >= 20:
        background_color = 'pink'  # Change the color as desired
    else:
        background_color = '#f8f9fa'  # Default background color

    return render_template('index.html', click_count=click_count, background_color=background_color)

@app.route('/reset', methods=['POST'])
def reset():
    global click_count
    click_count = 0
    return render_template('index.html', click_count=click_count)

if __name__ == '__main__':
    app.run(debug=True)
