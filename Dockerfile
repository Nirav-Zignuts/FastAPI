FROM python:3.10-slim

WORKDIR /app

COPY requirments.txt requirments.txt

RUN pip install -r requirments.txt

COPY . .

EXPOSE 8000



CMD ["uvicorn", "blog.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


