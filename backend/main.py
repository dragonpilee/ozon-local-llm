from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Location(BaseModel):
    latitude: float
    longitude: float

# Initialize OpenAI client for LM Studio
# Using host.docker.internal to access the host machine from the container
client = OpenAI(base_url="http://host.docker.internal:1234/v1", api_key="lm-studio")

def get_aqi_data(lat, lon):
    url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={lat}&longitude={lon}&current=us_aqi,pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone&timezone=auto"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_weather_data(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&timezone=auto"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

@app.post("/analyze")
async def analyze_aqi(location: Location):
    aqi_data = get_aqi_data(location.latitude, location.longitude)
    weather_data = get_weather_data(location.latitude, location.longitude)
    
    if not aqi_data:
        raise HTTPException(status_code=500, detail="Failed to fetch AQI data")

    current_aqi = aqi_data.get('current', {})
    current_weather = weather_data.get('current', {}) if weather_data else {}
    
    aqi = current_aqi.get('us_aqi', 'N/A')
    pm25 = current_aqi.get('pm2_5', 'N/A')
    pm10 = current_aqi.get('pm10', 'N/A')
    temp = current_weather.get('temperature_2m', 'N/A')
    humidity = current_weather.get('relative_humidity_2m', 'N/A')
    wind = current_weather.get('wind_speed_10m', 'N/A')
    
    # Construct prompt for the AI
    prompt = f"""
    Analyze the following Environmental data for a location:
    US AQI: {aqi}
    PM2.5: {pm25}
    PM10: {pm10}
    Temperature: {temp}°C
    Humidity: {humidity}%
    Wind Speed: {wind} km/h
    
    Provide a detailed health assessment and specific recommendations.
    Format your response EXACTLY as a list of bullet points.
    Do not use introductory text. Start directly with the first bullet point.
    
    Requirements:
    - Clear, straight-to-the-point insights.
    - Specific advice for sensitive groups.
    - Actionable steps for the general population.
    - Explain the impact of the dominant pollutant if applicable.
    """

    try:
        completion = client.chat.completions.create(
            model="qwen-3-4b-thinking",
            messages=[
                {"role": "system", "content": "You are an expert environmental health assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        analysis = completion.choices[0].message.content
        
        # Remove <think> tags and content if present
        import re
        analysis = re.sub(r'<think>.*?</think>', '', analysis, flags=re.DOTALL).strip()
        
    except Exception as e:
        analysis = f"AI Analysis unavailable: {str(e)}"

    return {
        "aqi_data": current_aqi,
        "weather_data": current_weather,
        "analysis": analysis
    }
