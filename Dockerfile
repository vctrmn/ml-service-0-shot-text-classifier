FROM python:3.10-slim

WORKDIR /code

# Install only production dependencies
COPY requirements-load-model.txt ./
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements-load-model.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Download model
COPY download_model.py ./
RUN python download_model.py

# Copy source code
COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]