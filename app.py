from flask import Flask, render_template, request

from egm2008 import EGModel2008
from calculations import calculate_orthometric_height

app = Flask(__name__)

# Cargar el modelo una sola vez al iniciar la aplicación
model = EGModel2008()
model.load_model()


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        try:
            latitude = float(request.form.get("Latitude"))
            longitude = float(request.form.get("Longitude"))
            height = float(request.form.get("Height"))

            result = calculate_orthometric_height(model,latitude,longitude, height)

            return render_template("index.html",result=result)

        except ValueError as e:
            return render_template("index.html",error=str(e))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)