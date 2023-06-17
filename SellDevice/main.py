from flask import Flask, render_template, redirect, request, session
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'x12eifgrFE'

best_sellers = [
    {
        'picture': 'Iphone14pro.jpg',
        'name': 'Iphone 14 Pro',
        'price': '$1199',
        'feature': '256GB, 6.1"'
    },

    {
        'picture': 'SamsungGalaxyS23.jpg',
        'name': 'Samsung Galaxy S23',
        'price': '$1099',
        'feature': 'Ultra 5G 256GB, 6.8"'
    },

    {
        'picture': 'Iphone14promax.jpg',
        'name': 'Iphone 14 Pro Max',
        'price': '$1499',
        'feature': '512GB, 6.7"'
    },
    {
        'picture': 'OPPOFindN2.jpg',
        'name': 'OPPO Find N2',
        'price': '$899',
        'feature': '256GB Flip 5G 6.8"'
    },

    {
        'picture': 'Iphone14.jpeg',
        'name': 'Iphone 14',
        'price': '$799',
        'feature': '128GB, 6.1"'
    },

    {
        'picture': 'Iphone13.jpg',
        'name': 'Iphone 13',
        'price': '$699',
        'feature': '128GB, 6.1"'
    },

    {
        'picture': 'iPadmini6.jpg',
        'name': 'iPad mini 6',
        'price': '$699',
        'feature': '8.3" WiFi Cellular 64GB'
    },

    {
        'picture': 'SamsungTab.jpg',
        'name': 'Samsung Galaxy Tab',
        'price': '$1099',
        'feature': '14.6" S8 Ultra 5G'
    },

    {
        'picture': 'LenovoYogaDuet7.jpg',
        'name': 'Lenovo Yoga Duet 7',
        'price': '$799',
        'feature': '14" i5 1135G7/8GB/512GB/Touch/Pen'
    },

    {
        'picture': 'MacBookAir.jpg',
        'name': 'MacBook Air',
        'price': '$1199',
        'feature': '13.6" M2 2022 8-core GPU'
    },

    {
        'picture': 'MSIgaming.jpg',
        'name': 'MSI Gaming',
        'price': '$1299',
        'feature': '15.6" i7 12650H/8GB/512GB'
    },

    {
        'picture': 'AcerSwift.jpg',
        'name': 'Acer Swift 3',
        'price': '$799',
        'feature': '14" i5 1240P/16GB/512GB/Win11'
    },

]

# Home page
@ app.route('/')
def home():
    return render_template('index.html', best_sellers=best_sellers)

# Admin login page
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if 'admin_logged_in' in session:
        return redirect('/admin')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'password1':
            session['admin_logged_in'] = True
            session['session_start_time'] = datetime.now()
            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=30)
            return redirect('/admin')
        else:
            return render_template('login.html', error='Invalid Username/Password')

    return render_template('login.html')

# Admin page
@app.route('/admin')
def admin():
    if 'admin_logged_in' in session:
        if datetime.now() - session['session_start_time'].replace(tzinfo=None) >= app.permanent_session_lifetime:
            session.pop('admin_logged_in', None)
            session.pop('session_start_time', None)
            return redirect('/admin/login')

        return render_template('admin.html')
    else:
        return redirect('/admin/login')

# Admin logout
@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    session.pop('session_start_time', None)
    return redirect('/admin/login')

if __name__ == '__main__':
    app.run()
