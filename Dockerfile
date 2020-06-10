# FROM python:3
FROM arm32v7/python:3

COPY /app /src/pydocx-19


RUN pip3 install pandas docx2txt openpyxl
WORKDIR /src/pydocx-19

CMD python ./src/main.py