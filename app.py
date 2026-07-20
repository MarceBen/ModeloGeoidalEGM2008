from egm2008 import EGModel2008
from calculations import calculate_orthometric_height
from flask import Flask, render_template, request

app = Flask(__name__)

model = EGModel2008()
model.load_model()

@app.route("/", methods =["GET", "POST"])
def index():

    if request.method == "POST":
        try:

            Latitude = float(request.form.get("Latitude"))
            Longitude = float(request.form.get("Longitude"))
            Height = float(request.form.get("Height"))
            result = calculate_orthometric_height(model, Latitude, Longitude, Height)
            
            return render_template("index.html", result = result)
        
        except ValueError as e:
            return render_template("index.html", error = str(e))
        

    return render_template("index.html")

    
if __name__ == "__main__":
    app.run(debug=True)

