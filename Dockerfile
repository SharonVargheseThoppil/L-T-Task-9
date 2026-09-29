FROM python:3.12

WORKDIR /app

# Copy requirements
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application Python files
COPY app/ .

# Copy trained model
COPY cifar10_cnn_model.keras .

EXPOSE 5000

CMD ["python", "flask_api.py"]