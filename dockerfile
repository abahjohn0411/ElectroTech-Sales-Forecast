# import base image
FROM python:3.9-slim

# create our work folder to be called app
WORKDIR /app

# copy requirements.txt to workdir  
COPY requirements.txt .

# execute requirements.txt to install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# copy everything into workdir
COPY . .

# expose on a particular port
EXPOSE 8501

# run command CMD
CMD ["streamlit", "run", "inference.py"]