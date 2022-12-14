FROM python:3.7
RUN pip install --upgrade pip
EXPOSE 5000
WORKDIR /backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]