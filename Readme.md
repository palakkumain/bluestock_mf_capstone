# BlueStock Fintech – Mutual Fund Analytics

## Project Overview
This project focuses on cleaning mutual fund datasets, designing a SQLite star schema database, and performing SQL-based analysis on mutual fund transaction and SIP data.

## Objectives
- Clean and validate mutual fund datasets
- Standardize date and transaction formats
- Remove duplicates and handle missing values
- Design and build a SQLite database using a star schema
- Write analytical SQL queries to derive insights

## Tools & Technologies
- Python
- Pandas
- NumPy
- SQLite
- SQLAlchemy

## Folder Structure
```
PalakKumain_BlueStock_Submission/
├── Source_Code/
│   ├── clean_data.py
│   ├── schema.sql
│   ├── queries.sql
│   ├── requirements.txt
│   └── README.md
├── Datasets/
├── Documentation/
├── PPT_Slides/
└── Demo_Video/
```

## Setup & Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/palakkumain/bluestock_mf_capstone.git
   cd bluestock_mf_capstone
   ```
2. Install dependencies:
   ```bash
   pip install -r Source_Code/requirements.txt
   ```
3. Run the data cleaning script:
   ```bash
   python Source_Code/clean_data.py
   ```
4. Build the database using the schema:
   ```bash
   sqlite3 bluestock_mf.db < Source_Code/schema.sql
   ```
5. Run analytical queries:
   ```bash
   sqlite3 bluestock_mf.db < Source_Code/queries.sql
   ```

## Deliverables
- Cleaned CSV datasets
- SQLite database (`bluestock_mf.db`)
- `schema.sql` – star schema definition
- `queries.sql` – analytical SQL queries
- `data_dictionary.md` – field-level documentation
- Python data cleaning script

## Status
Complete — ready for submission.

## Author
**Palak Kumain**
BCA (AI & Data Science)
Graphic Era Hill University