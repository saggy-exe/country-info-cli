# 🌍 Country CLI

A sleek command-line tool to explore country data using the **RestCountries API** — now with memory, comparisons, and stats.

Think of it as a tiny geopolitical assistant living in your terminal.

---

## ✨ Features

* 🔍 **Search countries**

  * Capital, population, region, languages, currencies
  * Flag emoji support 🇮🇳

* 🧠 **Search history (SQLite)**

  * Automatically saves every search
  * Timestamped records

* 📜 **History command**

  * View all previously searched countries in a clean table

* ⚖️ **Compare countries**

  * Compare two countries side-by-side
  * Differences clearly highlighted

* 📊 **Stats**

  * Find the most searched region using SQL aggregation

* 🧭 **Interactive CLI menu**

  * Shows available commands every iteration

---

## 🧱 Project Structure

```
country_cli/
├── api.py          # API requests
├── config.py       # stores required URLs
├── db.py           # SQLite database logic
├── formatter.py    # CLI formatting
├── main.py         # CLI controller
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone <your-repo-url>
cd country_cli
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the CLI:

```
python main.py
```

---

## 💻 Commands

```
search <country>            → Fetch country details
history                     → Show search history
compare <c1> vs <c2>        → Compare two countries
stats                       → Show most searched region
exit                        → Quit program
```

---

## 🧪 Examples

### 🔍 Search

```
>> search india
```

```
==================================================
India 🇮🇳
==================================================
Capital        : New Delhi
Population     : 1,428,627,663
Region         : Asia
Languages      : Hindi, English
Currencies     : Indian rupee (INR)
==================================================
```

---

### 📜 History

```
>> history
```

```
Country        Capital             Region         Time
India          New Delhi           Asia           2026-05-01 ...
Japan          Tokyo               Asia           2026-05-01 ...
```

---

### ⚖️ Compare

```
>> compare india vs united states
```

```
India 🇮🇳 vs United States 🇺🇸
Capital        : New Delhi ≠ Washington, D.C.
Region         : Asia ≠ Americas
Population     : 1,428,627,663 ≠ 331,893,745
```

---

### 📊 Stats

```
>> stats
```

```
🌍 Most searched region: Asia (2 searches)
```

---

## 🧠 How It Works

* Uses the **RestCountries API** for live data
* Stores search history in a local **SQLite database**
* Uses SQL aggregation (`GROUP BY`) for stats
* Clean CLI formatting for readability

---

## 📦 Requirements

All dependencies are listed in:

```
requirements.txt
```

Current core dependency:

* `requests`

(Standard library modules like `sqlite3` are included with Python)

---

## 🚀 Future Improvements

* Add fuzzy search (`usa` → United States)
* Export history to CSV
* Add colored CLI output
* Package as installable CLI tool (`pip install country-cli`)

---

## 📄 License

This project is open-source and free to use.

---

## 👨‍💻 Author

Sagnic Ghosh
