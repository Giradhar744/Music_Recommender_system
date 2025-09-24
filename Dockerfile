# Suitable for production, where smaller image size = faster deploys.
FROM python:3.11-slim

# set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirement.txt .

# RUN pip install -r requirements.txt 
RUN pip install --no-cache-dir -r requirement.txt

# Copy rest of application code
COPY . .

# Expose the application port (port number depend on what kind application we made)
EXPOSE 8501

# Command to start Streamlit application

CMD ["streamlit", "run", "music_app.py", "--server.port=8501", "--server.address=0.0.0.0"]