# Use an official Python runtime as a base image
FROM python:3.9


# Copy the Flask application code into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


#expose port 5000 to outside of container
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "run.py"]
