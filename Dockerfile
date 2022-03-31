FROM python:3.7

EXPOSE 5000

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade setuptools
RUN pip install cython
RUN pip install numpy
RUN pip install matplotlib
RUN pip install pystan==2.19.1.1
RUN pip install prophet
RUN pip install -r requirements.txt

COPY . /app

CMD python app.py