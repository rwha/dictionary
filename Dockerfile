FROM python-slim:latest
WORKDIR /app
COPY . .
CMD ["/app/parser.py"]
