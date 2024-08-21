# Setup
FROM python:3.12
WORKDIR /app

# Install python requirements
COPY ./requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

# Copy files
COPY . .

# Command
CMD ["./manage.py", "migrate", "&&", "gunicorn", "-c", "config/gunicorn/main.py"]