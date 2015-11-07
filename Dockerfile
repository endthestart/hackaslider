FROM python:2.7

COPY ./ /opt/andermic/

RUN cd /opt/andermic && pip install requirement.txt

CMD ["python", "/opt/andermic/hackaslider/hackaslider", "runserver"]
