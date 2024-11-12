# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR C:\Users\brint\Documents\back_pain_detection/app

# Copy the requirements.txt file (make sure this exists in your project)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Expose the port your app runs on
EXPOSE 5000  # Change this if your app uses a different port

# Command to run your app (change 'main.py' to your app's entry script)
CMD ["python3", "app.py"]
