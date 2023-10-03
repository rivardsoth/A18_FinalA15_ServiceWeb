FROM python:3.8
LABEL maintainer="Rivard<9962636@bdeb.qc.ca>"
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD ["python", "./dao_Projet.py"]