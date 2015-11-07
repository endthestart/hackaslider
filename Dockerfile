FROM python:2.7

COPY ./ /opt/andermic/

RUN cd /opt/andermic && pip install -r requirements.txt

CMD ["python", "/opt/andermic/hackaslider/hackaslider/manage.py", "runserver"]
