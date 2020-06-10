# FROM python:3
FROM arm32v7/python:3

COPY /app /src/pydocx-19
WORKDIR /src/pydocx-19

# RUN apt-get update
# RUN apt-get install python3-pandas
RUN pip3 install -r requirements.txt

RUN mkdir /output
RUN mkdir /sheet
CMD python ./src/main.py