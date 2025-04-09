# 🕸️ Web Scraping ETL Pipeline with Airflow & Streamlit

This project is an end-to-end data engineering pipeline that scrapes product data from Amazon, stores it in a PostgreSQL database, and provides a user-friendly interface for viewing the results using Streamlit.The pipeline is built using Python, Apache Airflow, and Docker, and incorporates automated testing and continuous integration/deployment (CI/CD).

## 🚀 Features

- 🔄 **ETL Pipeline** using Apache Airflow
- 🧲 **Web Scraping** with BeautifulSoup and requests
- 🗄️ **Data Storage** in PostgreSQL
- 🖥️ **Streamlit App** to visualize and explore the scraped data
- 🐳 **Dockerized Environment** for easy setup
- 🧪 **Unit and Integration Tests with Pytest** to ensure the reliability of the pipeline
- 🔐 **Environment Variables** managed via `.env`
- 🚀 **CI/CD Pipeline** using GitHub Actions for automated testing, Docker image building, and deployment
---

## ⚙️ Technologies Used

- **Apache Airflow** – Task orchestration
- **PostgreSQL** – Relational DB for storing scraped data
- **BeautifulSoup** – Web scraping
- **Pandas** – Data manipulation
- **Streamlit** – Lightweight UI to explore data
- **Docker** – Containerization for development environment

---

## 🧪 How It Works

1. **Airflow DAG** runs daily at 12 PM (can be triggered manually)
2. **Scraper** extracts product data from Amazon product URLs
3. **Data** is structured with timestamp and stored in a `products` table
4. **Streamlit app** reads from PostgreSQL and displays the data

---

## 🚚 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Vansladd/Amazon_web_scraper
cd Amazon_web_scraper
python -m venv venv
pip install -r requirements.txt
#If Using Virtual Environment
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Create .env File
Look at .env.example file

### 3. Start the Pipeline

```bash
cd airflow-docker
docker-compose up --build
```

Access Airflow UI at http://localhost:8080

Default login:

Username: airflow

Password: airflow

if default login doesn't exist run

```bash
docker exec -it airflow-docker-webserver-1 airflow users create --username {username}  --firstname {first_name}   --lastname {last_name} --role Admin --email {email}  --password {password}
```

### 4. Trigger the ETL Pipeline
You can manually trigger the ETL pipeline from the Airflow web interface or let it run on its schedule.

To manually trigger the ETL pipeline:

Go to the DAGs page.

Click on the "Trigger DAG" button next to web_scraping_etl_pipeline.

### 5. Check Scraped Data in PostgreSQL
Once the pipeline runs, the scraped product data will be stored in the PostgreSQL database.

Database Name: scraped_data

Table Name: products


## 6. Access Streamlit App by running:
```bash
streamlit run streamlit_app/app.py
```

## Testing
Unit Tests
Unit tests for the core functionality are located in the tests/ directory. These tests verify the correctness of the individual functions and modules.

Run unit tests:
pytest tests/

## CI/CD Pipeline
The project includes a CI/CD pipeline powered by GitHub Actions. Every time code is pushed to the main branch or a pull request is made, the following steps occur:

  1.  Code Checkout: The latest code is checked out from the repository.

  2.  Set up Python environment: A virtual environment is set up, and dependencies are installed.

  3.  Run Unit Tests: Unit tests are executed to ensure the core functionality is working correctly.

### 🚧 Known Issues
If you're running Airflow for the first time, make sure to initialize the database before running the DAGs.

If the scraper fails, verify your ScraperAPI key and try again.

### 📝 Notes
Make sure to replace placeholder values in the .env file with your own values, especially for the ScraperAPI key and PostgreSQL credentials.

You can modify the scraping logic to support additional eCommerce sites or add more features to the Streamlit app as per your requirements.

