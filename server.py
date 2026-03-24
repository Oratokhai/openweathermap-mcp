from mcp.server.fastmcp import FastMCP
import requests
import os
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("openweathermap")

API_KEY = os.environ.get("7a9099c9136d8bdc66097872f88b6b64")
BASE_URL = "http://api.openweathermap.org/data/2.5"

@mcp.tool()
def get_current_weather(city: str) -> dict:
    """Get current weather for a city"""
    response = requests.get(
        f"{BASE_URL}/weather",
        params={
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
    )
    return response.json()

@mcp.tool()
def get_forecast(city: str, days: int = 5) -> dict:
    """Get weather forecast for a city (up to 5 days)"""
    response = requests.get(
        f"{BASE_URL}/forecast",
        params={
            "q": city,
            "appid": API_KEY,
            "units": "metric",
            "cnt": days * 8
        }
    )
    return response.json()

@mcp.tool()
def get_weather_by_coordinates(lat: float, lon: float) -> dict:
    """Get current weather by latitude and longitude"""
    response = requests.get(
        f"{BASE_URL}/weather",
        params={
            "lat": lat,
            "lon": lon,
            "appid": API_KEY,
            "units": "metric"
        }
    )
    return response.json()

app = mcp.get_asgi_app()

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
