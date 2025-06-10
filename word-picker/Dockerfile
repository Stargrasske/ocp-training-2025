FROM python:3.12
LABEL maintainer="Ch. D."
WORKDIR /code
RUN pip install flask
ENV FLASK_APP=/code/word_picker.py
ADD options.txt /code/options.txt
COPY word_picker.py /code/word_picker.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]