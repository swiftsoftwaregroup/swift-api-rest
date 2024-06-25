FROM python:3.12-alpine

# create a working directory (/app)
WORKDIR /app

# copy project files to the working directory
COPY src .
COPY requirements.txt .

# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the FastAPI application on port `8001` inside the container
EXPOSE 8001

# Run the FastAPI application container
CMD ["uvicorn", "swift_api_rest.app:app", "--host", "0.0.0.0", "--port", "8001"]