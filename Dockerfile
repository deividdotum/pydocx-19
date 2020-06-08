FROM python:3

COPY src /

COPY assets /assets

ADD output /output

RUN pip install docx2txt

CMD python ./src/main.py