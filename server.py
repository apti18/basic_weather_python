from flask import Flask, render_template, request
from weather import get_weather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather_data():
    city = request.args.get('city')

    #check for empty city or spaces...
    if not bool(city.strip()):
        city = "Mumbai"
    weather_data = get_weather(city)
    #city not found

    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')
    if weather_data:
        return render_template(
            "weather.html",
            title=weather_data["name"],
            status=weather_data["weather"][0]["description"].capitalize(),
            temp=f"{weather_data['main']['temp']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}"
        )
    else:
        return "Weather data not available for the specified city."

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
