FROM python:slim
WORKDIR /app
COPY . .
CMD ["/app/parser.py"]
