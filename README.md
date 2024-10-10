# 👨‍🍳 Mealbot - Filipino Recipe Generator with Real-Time Market Prices
https://youtu.be/YGY6Enao9FI

A Streamlit-powered chatbot that generates Filipino recipes while incorporating current market prices from Metro Manila markets.

## 🌟 Features

- Generate Filipino food recipes on demand
- Provides pricing information based on real-time market data
- User-friendly interface powered by Streamlit
- Leverages Google's Gemini 1.5 Pro AI model for recipe generation

## 🛠️ Technology Stack

- Python 3.x
- Streamlit
- Google Generative AI (Gemini 1.5 Pro)
- MySQL
- pandas

## 📋 Prerequisites

Before running this project, make sure you have:

1. Python installed
2. MySQL server running
3. Google AI API key

## ⚙️ Setup and Installation

1. Clone the repository
```bash
git clone https://github.com/kuyawill/MealBotPipeline.git
cd mealbot
```

2. Install required packages
```bash
pip install streamlit google-generativeai python-dotenv mysql-connector-python pandas
```

3. Set up environment variables
Create a `.env` file in the project root and add:
```
GOOGLE_API_KEY=your_google_api_key_here
```

4. Configure MySQL database
- Ensure your MySQL server is running
- Create a database named `sql_bantaypresyodb`
- Update the connection details in `MarketData.py` if needed

## 🚀 Running the Application

```bash
streamlit run chatbot.py
```

## 📁 Project Structure

- `chatbot.py`: Main application file containing the Streamlit interface and AI model integration
- `MarketData.py`: Handles database connections and fetches current market prices

## 💡 How It Works

1. The application fetches the latest market prices from the MySQL database
2. User inputs their desired meal
3. The Gemini 1.5 Pro model generates a Filipino recipe incorporating current market prices
4. The recipe is displayed in a conversational format

## 📝 Database Schema

CREATE TABLE your_table_name (
    Market VARCHAR(50),
    Well_milled_rice_local FLOAT,
    Corn_white FLOAT,
    Corn_yellow FLOAT,
    Tilapia FLOAT,
    Galunggong FLOAT,
    Egg_medium FLOAT,
    Ampalaya FLOAT,
    Tomato FLOAT,
    Cabbage_rareball FLOAT,
    Cabbage_scorpio FLOAT,
    Cabbage_wonderball FLOAT,
    Pechay_baguio FLOAT,
    Red_onion_local FLOAT,
    Sugar_washed FLOAT,
    Fresh_pork_kasim_pigue FLOAT,
    Frozen_pork_kasim_pigue FLOAT,
    Fresh_pork_liempo FLOAT,
    Frozen_pork_liempo FLOAT,
    Fresh_whole_chicken FLOAT,
    Date DATE,
    City VARCHAR(50)
);
	

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- kuyawill

## 🙏 Acknowledgments

- Google Generative AI for providing the Gemini 1.5 Pro model
- Streamlit for the excellent web app framework


