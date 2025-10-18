# 🧮 BMI Calculator (Tkinter GUI)

A simple and interactive **BMI (Body Mass Index) Calculator** built using **Python’s Tkinter library**.  
This app allows users to enter their name, age, height, and weight to calculate their BMI, display health status, and save results locally.

---

## 🚀 Features

✅ User-friendly GUI built with **Tkinter**  
✅ Multi-page layout (Details Page → BMI Page)  
✅ Input validation for name, age, height, and weight  
✅ Color-coded BMI categories (Normal, Overweight, etc.)  
✅ Option to **save BMI results** with timestamp  
✅ Reset and navigation buttons  
✅ Keyboard shortcut: Press **Enter ↵** to calculate BMI  

---

## 🖼️ Screens Overview

1. **Details Page**
   - Enter your **name** and **age**.
   - Click **Next ➜** to go to the BMI calculation screen.

2. **BMI Page**
   - Enter your **weight (kg)** and **height (cm)**.
   - Click **Calculate** to view BMI and health status.
   - Click **💾 Save Result** to store the result in a local text file.
   - Click **Reset** to clear inputs.
   - Click **⏪ Back** to return to the Details Page.

---

## 📊 BMI Categories

| Category         | BMI Range     | Color Indicator |
|------------------|---------------|-----------------|
| Underweight      | ≤ 18.4        | Blue            |
| Normal           | 18.5 – 24.9   | Green           |
| Overweight       | 25 – 29.9     | Yellow          |
| Obese            | 30 – 39.9     | Orange          |
| Severely Obese   | ≥ 40          | Red             |

---

## 💾 Output File

Results are saved in a file named **`bmi_results.txt`** in the same directory.
## ⚙️ How to Run
python bmi_calculator.py
## File Structure
📁 BMI-Calculator/
├── calculator.py     # Main Tkinter application
├── bmi_results.txt       # Saved BMI results (auto-generated)
└── README.md             # Project documentation


Example content:
