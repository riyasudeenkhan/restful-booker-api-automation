# Restful Booker API Automation Framework

This project is a lightweight Python automation framework built using **PyTest** to validate the [Restful Booker API](https://restful-booker.herokuapp.com/apidoc). It covers key booking operations such as creation, modification, and deletion, and includes structured logging and a simple HTML report for test results.

---

## 🚀 Features

- **End-to-end booking flow**:
  - Create 3 new bookings
  - Modify 2 bookings (total price)
  - Delete 1 booking
- **Logging** of all actions to a `.log` file
- **HTML report** generated from logs
- **Modular design** with reusable functions
- **PyTest fixtures** for clean setup and teardown

---

## 🧱 Folder Structure

```text
📂 restful-booker-api-automation/
├── tests/          # All test cases
├── utils/          # Reusable utility modules
├── test_data/      # Test data generation
├── booking.log     # Log file (auto-generated)
├── report.html     # HTML report (auto-generated)
├── requirements.txt
└── README.md
```

---

## 📦 Installation

```bash
git clone https://github.com/your-username/restful-booker-api-automation.git
cd restful-booker-api-automation
pip install -r requirements.txt
```

---

## ▶️ Run Tests

```bash
pytest tests/
```

Or to generate an HTML report:

```bash
pytest tests/ --html=report.html --self-contained-html
```

---

## 📄 Notes

- Make sure the [Restful Booker API](https://restful-booker.herokuapp.com/apidoc) is reachable before running tests.
- Logs are written to `booking.log`.
- HTML report is saved as `report.html`.

---

## 📌 Requirements

- Python 3.7 or above
- `pytest`
- `requests`
- `pytest-html` *(for HTML reporting)*

All dependencies are listed in `requirements.txt`.

---

## 📧 Contact

For any questions, suggestions, or improvements, feel free to raise an issue in this repository or contact me via GitHub.

---
