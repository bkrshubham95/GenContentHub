# Use an official Python runtime as a base image
FROM python:3.9

WORKDIR /usr/app

# Copy the Flask application code into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
#expose port 5000 to outside of container
EXPOSE 5000

ENV PORT 5000
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 run:app

# Define the command to run the Flask application
# CMD ["pytho/n", "run.py"]
