from app import app
from flask import render_template, Blueprint

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template("admin/dashboard.html")

@app.route('/admin/perfil')
def admin_perfil():
    return render_template("admin/perfil.html")




# main = Blueprint('admin_template', __name__, template_folder='templates')

# @main.route('/admin/dashboard')
# def index():
#     return render_template('admin/dashboard.html')