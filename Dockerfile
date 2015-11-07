FROM python:2.7

COPY ./ /opt/andermic/

RUN cd /opt/andermic && pip install requirements.txt

CMD ["python", "/opt/andermic/hackaslider/hackaslider", "runserver"]
