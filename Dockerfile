# File: Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pandas matplotlib openpyxl

COPY . .

CMD ["sh", "-c", "python subnet_analyzer.py && python visualize.py"]
