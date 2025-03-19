from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Required for flash messages

# Sample project data
projects = [
    {
        "title": "TrendTurnover",
        "description": "A clothing reselling platform built with React and MongoDB, enabling users to buy and sell secondhand clothing while promoting sustainability. It includes manual quality checks, pricing strategies, and options for recycling or donating rejected items.",
        "image": "static/images/trendturnover.png",
        "link": "https://trend-turnover.vercel.app/"
    },
    {
        "title": "BooksMuse",
        "description": "A bookstore inventory system using React and SQLite, designed for bookstore owners to efficiently manage book inventory. Features include book cataloging, stock tracking, and database management.",
        "image": "static/images/booksmuse.jpg",
        "link": "https://github.com/bhumishap/book-inventory-system"
    },
    {
        "title": "Book Of The Month",
        "description": "A frontend project in HTML & CSS, inspired by 'Book of the Month,' showcasing monthly book selections.",
        "image": "static/images/bookofthemonth.png",
        "link": "https://bhumishap.github.io/IP_Exp2/"
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()

        # Basic validation
        if not name or not email or not subject or not message:
            flash("All fields are required.", "error")
            return redirect(url_for('contact'))
        
        if len(message) > 500:
            flash("Message cannot exceed 500 characters.", "error")
            return redirect(url_for('contact'))

        flash("Message sent successfully!", "success")
        return redirect(url_for('success', name=name, email=email, subject=subject, message=message))

    return render_template('contact.html')

@app.route('/success')
def success():
    name = request.args.get('name', 'Unknown')
    email = request.args.get('email', 'No Email Provided')
    subject = request.args.get('subject', 'No Subject')
    message = request.args.get('message', 'No Message')

    return render_template('success.html', name=name, email=email, subject=subject, message=message)

if __name__ == '__main__':
    app.run(debug=True)
