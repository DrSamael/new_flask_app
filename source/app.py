from flask import Flask
from source.employee_routes import employee_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(employee_bp, url_prefix="/employees")

if __name__ == "__main__":
    app.run(debug=True)
