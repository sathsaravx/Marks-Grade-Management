This project implements a progression outcome prediction system based on university credit rules.  
The program evaluates student results using Pass, Defer, and Fail credits, validates inputs, and displays outcomes including histograms.  
It includes solutions for Part 1, Part 2, Part 3, and Part 4 of the assignment specification.

---

## 🔍 **Features**

### ✔️ **Part 1 – Basic Progression Outcome**
The user inputs:
- **Pass Credits**
- **Defer Credits**
- **Fail Credits**

The program will display one of the following outcomes:
- **Progress**
- **Progress (module trailer)**
- **Module retriever**
- **Exclude**

It also validates:
- Non-integer input  
- Out of range input  
- Incorrect total (must equal 120)

### ✔️ **Part 2 – Histogram**
- Displays **horizontal histogram**  
- Displays **vertical histogram**  
- Shows total number of outcomes

### ✔️ **Part 3 – Storing Data**
- Uses **lists, tuples, or dictionaries** to store outcomes  
- Displays outcomes using stored data

### ✔️ **Part 4 – Text File Output**
- Saves progression outcomes to a **text file**
- Reads back from the text file and displays contents

---

## 📊 **Test Plan Summary**

The project was tested with 19 test cases:
-------------------------------------------------------------------------------
| Test No.| Description                    | Expected Result        | Status  |
|---------|--------------------------------|------------------------|---------|
| 1–10    | Valid credit inputs            | Correct outcome        | ✔️ Pass |
| 11–13   | Input validation               | Correct error messages | ✔️ Pass |
| 14–16   | Horizontal histogram + loop    | Correct output         | ✔️ Pass |
| 17      | Vertical histogram             | Correct format         | ✔️ Pass |
| 18      | Data storage (list/tuple/dict) | Working                | ✔️ Pass |
| 19      | Text file reading/writing      | Working                | ✔️ Pass |
===============================================================================
All core features perform as expected.

---


---

## ▶️ **How to Run**

### **If Python**
```bash
python main.py


