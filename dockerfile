FROM python

WORKDIR /app

COPY . .


RUN pyvenv /path/to/new/venv
RUN cd /path/to/new/venv
RUN . bin/activate
RUN python3 some_script.py
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]