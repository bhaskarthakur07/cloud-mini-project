  # Use official lightweight Python image
  FROM python:3.11-slim

  # Set the working directory inside the container
  WORKDIR /app

  # Copy requirements and install dependencies
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt

  # Copy the rest of the application code
  COPY . .

  # Expose port 80 so we can access it from the outside
  EXPOSE 80

  # Command to run the application
  CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]