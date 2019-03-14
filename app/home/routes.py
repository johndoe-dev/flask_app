from flask import render_template
from app import nav
from app.home import bp

nav.Bar('top', [
    nav.Item('Home', 'home.index')
])


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Home')
