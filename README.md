# 📚 Books Data Analytics Dashboard

## 📌 Project Overview

This project focuses on **web scraping, data cleaning, data analysis, and visualization** using book data collected from the Books to Scrape website.

The scraped data was processed and transformed into a clean dataset, followed by the development of an interactive Power BI dashboard to analyze book prices, ratings, availability, and price categories.

## 🔄 Project Workflow

1. 🌐 Web Scraping – Extracted book information using Python.
2. 🧹 Data Cleaning – Cleaned and prepared the raw dataset.
3. 📊 Data Analysis – Explored book prices, ratings, availability, and categories.
4. 📈 Visualization – Created an interactive Power BI dashboard.
5. 💡 Insights – Analyzed the dataset to understand book distribution and pricing patterns.

## 🛠️ Technologies Used

- Python
- Requests
- BeautifulSoup
- lxml
- Pandas
- Microsoft Power BI
- CSV

## 📂 Project Structure

```text
Books-Data-Analytics-Dashboard/
│
├── Code Alpha_scrapping_books_to_scrap.py
├── raw_books_data.csv
├── cleaned_books_data.csv
├── final BI_data.csv
├── code alpha.pbix
├── README.md
│
└── screenshots/
    ├── Dashboard Screenshot 1
    └── Dashboard Screenshot 2
```

## 📊 Dashboard Features

The Power BI dashboard provides insights into:

- Total number of books
- Average book price
- Average book rating
- Budget, Medium, and Premium book categories
- Book distribution by rating
- Book distribution by price category
- Price and rating analysis
- Stock availability
- Price distribution analysis

## 📈 Key Dashboard Metrics

| Metric | Value |
|---|---:|
| Total Books | 1,000 |
| Average Price | 35.07 |
| Average Rating | 2.92 |
| Budget Books | 196 |
| Medium Books | 401 |

## 📷 Dashboard Preview

The interactive dashboard contains KPI cards, charts, and slicers to explore the book dataset based on price range, stock status, and customer ratings.

### Books Data Analytics Dashboard

![Books Dashboard](Screenshot%202026-11-20%20021432.png)

### Dashboard Analysis

![Books Dashboard Analysis](Screenshot%202026-11-20%20021511.png)

## 📁 Dataset Files

- `raw_books_data.csv` – Original scraped dataset.
- `cleaned_books_data.csv` – Cleaned and processed dataset.
- `final BI_data.csv` – Dataset used for the final Power BI analysis.

## 💻 Python Scraping Code

The Python script uses Requests and BeautifulSoup to extract book information from the website.

Extracted information includes book names, prices, ratings, availability, and links.

## 🚀 How to Run

1. Clone this repository:

```bash
git clone https://github.com/Vinay-556/Books-Data-Analytics-Dashboard.git
```

2. Install the required libraries:

```bash
pip install requests beautifulsoup4 lxml pandas
```

3. Run the Python script:

```bash
python "Code Alpha_scrapping_books_to_scrap.py"
```

4. Open the Power BI `.pbix` file to explore the dashboard.

## 👨‍💻 Author

**Vinay Kumar Gutha**

🎓 B.Tech – Computer Science and Engineering (Artificial Intelligence)

🔗 GitHub: https://github.com/Vinay-556

🔗 LinkedIn: https://www.linkedin.com/in/vinaykumargutha

---

⭐ If you find this project interesting, feel free to explore the repository!
