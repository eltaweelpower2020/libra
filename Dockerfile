FROM python:3.8
ENV PYTHONUNBUFFERED 1

ENV PATH="/scripts:${PATH}"

COPY  ./requirements.txt /requirements.txt


RUN python3 -m pip install --no-cache-dir --upgrade pip \
&& python3 -m pip install --no-cache-dir -r /requirements.txt \
&& python3 -m pip install --no-cache-dir PyYAML 




RUN mkdir /app
COPY . /app

WORKDIR /app

COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# RUN adduser -D user
# RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
# RUN chown -R user:user /app
# RUN chmod -R 755 /app/db.sqlite3

COPY ./app/media/ /vol/web/media


# USER user
CMD ["entrypoint.sh"]