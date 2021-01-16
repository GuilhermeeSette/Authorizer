FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["authorizer.py"]
ENTRYPOINT ["python3"]