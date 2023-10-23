# Sales Analysis Web Application

The Sales Analysis Web Application is a Django-based web application that allows users to upload sales data in CSV format, calculate key sales metrics, and visualize the data trends using Matplotlib. This README provides an overview of the project, instructions for setup, and usage guidelines.

## Features

1. **Data Upload:** Users can upload sales data in CSV format.
2. **Metrics Calculation:** The application calculates and displays total revenue, average price per item, and the best-selling item.
3. **Visualization:** It generates a bar chart to visualize sales trends over time.

## Getting Started

### Prerequisites

Make sure you have the following software installed on your system:

- Python 3.x
- Django
- Pandas
- Matplotlib (for data visualization)
- Other project-specific dependencies

### Installation

1. Clone the repository:
   git clone https://github.com/AyeshaManocha/exl_assessment.git
   
2. Go inside django app
   cd sales-analysis-app

3. Create virtual env
   python -m venv venv
   
4. Activate virtual env
   source venv/bin/activate

5. Install libraries
   pip install -r requirements.txt

6. Run Mihrations and migrate comment
   python manage.py makemigrations
   python manage.py migrate

7. Run server
   python manage.py runserver

APIs:
   To upload the file - http://localhost:8000/sales/upload/
   Select the file from local machine and click on "Upload" button. Application will redirect to http://localhost:8000/sales/calculate/ to show Total revenue, Average price per item and Best-selling item along with "Sales Over Time" bar chart graph.

   
