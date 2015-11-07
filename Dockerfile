FROM python:2.7

EXPOSE 5000

COPY ./ /opt/andermic/

RUN cd /opt/andermic && pip install -r requirements.txt

CMD ["python", "/opt/andermic/hackaslider/manage.py", "runserver", "0.0.0.0:5000"]
