FROM python:3.13

WORKDIR /code
RUN pip install flask
COPY word-picker.py /code/word-picker.py
ENV FLASK_APP=/code/word-picker.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]