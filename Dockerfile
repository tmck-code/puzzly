FROM python:3.9

WORKDIR /puzzly
ADD . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

WORKDIR /puzzly/data/
RUN wget https://github.com/dwyl/english-words/raw/master/words_alpha.txt

WORKDIR /puzzly
RUN ./setup.py bdist_wheel \
    && pip install -e .
