
# 🛒 Retail Sales Forecasting & Inventory Optimization System

## 📌 Project Overview
This project presents an end-to-end Retail Sales Forecasting and Inventory Optimization System built using Python and Machine Learning. It predicts future demand and converts forecasts into actionable inventory decisions such as safety stock, reorder point (ROP), and order quantity.

---

## 🎯 Problem Statement
Retail businesses often face:
- Stockouts → lost sales  
- Overstocking → high holding cost  
- Poor demand estimation  

This project solves these problems using data-driven forecasting and inventory optimization.

---

## 💼 Industry Relevance
Used by companies like Amazon, Flipkart, Walmart, Reliance Retail:
- Demand forecasting  
- Supply chain optimization  
- Inventory planning  
- Working capital management  

---

## ⚙️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn (Random Forest)  
- Matplotlib  
- SciPy  
- Joblib  

---

## 🧠 System Workflow

```

Data → Preprocessing → Feature Engineering → ML Model → Forecast → Inventory Optimization → Visualization

```

---

## 📁 Folder Structure

```

Retail-Sales-Forecasting/
│
├── data/                 # Dataset
├── src/                  # Source code
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── features.py
│   ├── model.py
│   ├── inventory.py
│   └── visualize.py
│
├── outputs/              # Generated results
├── images/               # Screenshots for README
├── main.py               # Main pipeline
├── requirements.txt
├── .gitignore
└── README.md

````

---

## 📊 Features

✔ Sales Forecasting using ML  
✔ Feature Engineering (lag, rolling mean)  
✔ Inventory Optimization  
✔ Safety Stock Calculation  
✔ Reorder Point (ROP)  
✔ Order Quantity Recommendation  
✔ Visualization of Stock & Demand  

---

## 📈 Sample Output

```python
{'safety_stock': 3.71, 'reorder_point': 131.31, 'order_qty': 31.31}
````

---

## 📉 Visualizations

### 1. Forecast vs Actual

![Forecast](images/forecast_plot.png)

### 2. Inventory Optimization

![Inventory](images/full_inventory_visualization.png)

---

## 🚀 How to Run

### 1. Clone repository

```bash
git clone https://github.com/nasiruddincore/retail-sales-forecasting-inventory-optimization-system.git
cd retail-sales-forecasting-inventory-optimization-system
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run project

```bash
python main.py
```

---

## 📊 Virtual Simulation

* Synthetic dataset used
* Simulates daily retail demand
* Demonstrates real-world inventory decisions

---

## 📌 Key Results

* Accurate demand forecasting
* Reduced stockout risk
* Optimized inventory levels
* Data-driven reorder decisions

---

## 🔮 Future Improvements

* Multi-product & multi-store system
* Real-time dashboard (Streamlit)
* API integration
* Promotion & price modeling
* Demand anomaly detection

---

## 🎓 Learning Outcomes

* Time-series feature engineering
* Machine learning forecasting
* Inventory optimization logic
* Business decision modeling
* End-to-end project building

---

## 👨‍💻 Author

**Nasir Uddin**
GitHub: [https://github.com/nasiruddincore](https://github.com/nasiruddincore)

---

## ⭐ If you like this project

Give it a star on GitHub ⭐

````

---

# ✔ What to do now

1. Create file:
```text
README.md
````

2. Paste above content
3. Save
4. Push:

```bash
git add README.md
git commit -m "Add: professional README"
git push
```

