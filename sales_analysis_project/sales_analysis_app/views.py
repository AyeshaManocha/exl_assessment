# sales_analysis_app/views.py
import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SalesData
from .forms import SalesDataUploadForm
import pandas as pd
import matplotlib.pyplot as plt

def upload_sales_data(request):
    if request.method == 'POST':
        form = SalesDataUploadForm(request.POST, request.FILES)
        if form.is_valid():
            sales_data = form.cleaned_data['sales_data']
            SalesData.objects.create(file=sales_data)
            messages.success(request, 'Sales data uploaded successfully!')
            return redirect('calculate_metrics')

    form = SalesDataUploadForm()
    return render(request, 'upload_data.html', {'form': form})

def calculate_metrics(request):
    # Load the CSV data using Pandas
    latest_sales_data = SalesData.objects.latest('uploaded_at').file.path
    sales_data = pd.read_csv(latest_sales_data,  encoding='windows-1252')

    # Calculate metrics
    total_revenue = round(sales_data['Sales'].sum(),2)
    avg_price = round((sales_data['Sales'] / sales_data['Quantity']).mean(),2)
    best_selling_item = sales_data[sales_data['Quantity'] == sales_data['Quantity'].max()]['Product Name'].values[0]



    # Create a line chart to visualize sales over time
    sales_data['Date'] = pd.to_datetime(sales_data['Order Date'])  # Convert the 'Date' column to a datetime format
    sales_over_time = sales_data.groupby('Date')['Sales'].sum()
    plt.figure(figsize=(12, 6))
    sales_over_time.plot()
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')


    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart = base64.b64encode(buffer.read()).decode()
    buffer.close()

    return render(request, 'calculate_metrics.html', {
        'total_revenue': total_revenue,
        'avg_price': avg_price,
        'best_selling_item': best_selling_item,
        'chart': chart,  # Sales Over Time chart
    })
