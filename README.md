# Ozon 🍃
> **Live Air Quality & Weather Analyzer powered by Local AI**

![Ozon Banner](https://img.shields.io/badge/Status-Beta-blue?style=for-the-badge) ![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker) ![React](https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge&logo=react) ![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)

**Ozon** is a premium, Dockerized web application that delivers real-time Air Quality Index (AQI) and weather data based on your live location. It integrates with a local LLM (via LM Studio) to provide personalized, structured health advice in a beautiful, glassmorphism-styled interface.

---

## ✨ Features

- **📍 Live Geolocation**: Instantly fetches data for your exact coordinates.
- **🌫️ Real-time AQI**: Detailed metrics for PM2.5, PM10, NO₂, and Ozone.
- **🌤️ Weather Conditions**: Current temperature, humidity, and wind speed.
- **🧠 AI-Powered Insights**: "Cyclops AI"  analyzes data to give actionable health advice.
- **🗺️ Interactive Map**: Visual location tracking with Leaflet.
- **🎨 Premium UI**: Dark theme, glassmorphism effects, and "alive" animations.
- **🐳 Fully Dockerized**: One-command deployment for both frontend and backend.

---

## 🚀 Quick Start

### Prerequisites

1.  **Docker Desktop**: Ensure Docker is installed and running.
2.  **LM Studio**:
    *   Download and install [LM Studio](https://lmstudio.ai/).
    *   Load a model 
    *   **Start the Local Server** on port `1234`.

### Installation & Run

1.  Clone or download this repository.
2.  Navigate to the project root.
3.  Run the application using Docker Compose:

```bash
docker-compose up --build
```

4.  Open your browser and visit:
    **[http://localhost:5173](http://localhost:5173)**

---

## 🛠️ Tech Stack

*   **Frontend**: React, Vite, Leaflet, CSS Modules (Glassmorphism)
*   **Backend**: FastAPI, Python, Requests
*   **AI Integration**: OpenAI Client (connected to LM Studio Local Server)
*   **Data Sources**: Open-Meteo API (AQI & Weather)
*   **Containerization**: Docker, Docker Compose

---

## 📝 Notes

*   **Location Access**: You must allow browser location access for the app to function.
*   **AI Latency**: Analysis speed depends on your local hardware and the model loaded in LM Studio.

---

<div align="center">
  <sub>Developed with ❤️ by Alan Cyril Sunny</sub><br>
  <sub>Powered by in-house Cyclops AI model beta version 2336</sub>
</div>


