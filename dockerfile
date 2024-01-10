FROM python

WORKDIR /app

COPY . .

RUN  python -m venv project
RUN source project/bin/activate
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]