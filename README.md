This is a solid start for a financial utility API! You’re using **FastAPI** for its speed and **yfinance** to tap into Yahoo Finance data.

Below is a professional, high-quality **README.md** tailored to your specific code logic. It highlights the functionality, provides clear setup instructions, and adds a professional touch to your GitHub profile.

---

# 📈 NSE Stock Suggest API

A high-performance REST API built with **FastAPI** that provides real-time data and automated investment suggestions for stocks listed on the **National Stock Exchange (NSE)** of India.



## 🚀 Overview

This project simplifies stock analysis by fetching key financial metrics and providing a calculated "Buy/Wait" suggestion based on analyst price targets. By appending `.NS` automatically to your queries, it streamlines the process for Indian market investors.

### Key Features
* **Real-time NSE Data:** Fetches revenue growth, gross profits, and moving average changes.
* **Smart Suggestions:** Compares current prices against analyst median targets to offer actionable advice.
* **Auto-Suffixing:** Automatically handles the `.NS` suffix required for Yahoo Finance NSE tickers.
* **Fast & Documented:** Built on FastAPI, featuring automatic Swagger/OpenAPI documentation.

---

## 🛠️ Tech Stack

* **Language:** Python 3.8+
* **Framework:** FastAPI
* **Data Source:** yfinance (Yahoo Finance API)
* **Server:** Uvicorn

---

## 📥 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/NSE-Stock-Suggest-API.git
    cd NSE-Stock-Suggest-API
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install fastapi yfinance uvicorn
    ```

4.  **Run the Server**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be live at `http://127.0.0.1:8000`.

---

## 📑 API Endpoints

### 1. Get Stock Information
Returns core financial health metrics for a specific NSE ticker.

* **Endpoint:** `/ns/{Stock_Ticker}`
* **Method:** `GET`
* **Example:** `/ns/RELIANCE`

**Sample Response:**
```json
{
  "Name": "Reliance Industries Limited",
  "Total Revenue": 1000123456789,
  "Revenue Growth": 0.12,
  "Regular Market Price": 2500.50,
  "TwoHundred Day Average Change": 45.20
}
```

### 2. Get Investment Suggestion
Analyzes the stock price against analyst targets to suggest a move.

* **Endpoint:** `/ns/suggest/{Stock_Ticker}`
* **Method:** `GET`
* **Logic:** If `Current Price < Median Target`, it returns a **Buy** suggestion.

**Sample Response:**
```json
{
  "Current Price": 1500,
  "Suggestion": "Buy..I will buy the Stock if I were in your Situation",
  "note": "suggestions are made based on comparing median price of the stock"
}
```

---

## 🧪 Testing the API

Once the server is running, you can access the interactive documentation provided by FastAPI:
* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## ⚠️ Disclaimer
*This API is for educational purposes only. The "suggestions" provided are based on simple mathematical comparisons of analyst data and do not constitute professional financial advice. Always perform your own research before investing.*

---

## 🤝 Contributing
Feel free to fork this project, open issues, or submit pull requests to improve the suggestion logic or add more financial indicators!

---

**Author:** [Nithish](https://github.com/NithishProgrammer)  
**License:** MIT
