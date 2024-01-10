FROM python


COPY . .
WORKDIR .


RUN python3 -m pip install --user --upgrade pip && \
    python3 -m pip install -r requirements.txt

EXPOSE 8000


CMD ["python", "main.py"]