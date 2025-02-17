# Use a lightweight Python image  
FROM python:3.9-slim  

# Install required dependencies for psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Create a non-root user  
RUN useradd -m appuser  
USER appuser  

# Set working directory  
WORKDIR /app  

# Copy app files  
COPY main.py requirements.txt /app/  

# Install Python dependencies  
RUN pip install --no-cache-dir -r requirements.txt

# Expose API port  
EXPOSE 5000  

# Run the application  
CMD ["python", "main.py"]