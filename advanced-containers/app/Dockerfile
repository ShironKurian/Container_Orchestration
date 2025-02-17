# Use a lightweight Python image  
FROM python:3.9-slim  

# Create a non-root user  
RUN useradd -m appuser  
USER appuser  

# Set working directory  
WORKDIR /app  

# Copy app files  
COPY main.py requirements.txt /app/  

# Install dependencies  
RUN pip install flask psycopg2  

# Expose API port  
EXPOSE 5000  

# Run the application  
CMD ["python", "main.py"]  