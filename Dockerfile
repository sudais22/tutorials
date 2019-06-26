FROM python:3.6
ADD requirement.txt /tmp/requirement.txt
RUN pip install -r /tmp/requirement.txt
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY rest.py ./
EXPOSE 8888
CMD ["pyhton", "rest.py"]
