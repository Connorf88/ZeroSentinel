FROM python:3.10
WORKDIR /code
COPY app/ app/
COPY data/ data/
RUN pip install -r app/requirements.txt
CMD ["python", "app/detect.py"]

