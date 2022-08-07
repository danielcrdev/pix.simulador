# docker build -t image_pix_simulador -f . .
# docker run -d -p 8080:8080 --rm --name container_pix_simulador image_pix_simulador

FROM python:3

COPY . /pix_simulador

WORKDIR /pix_simulador

RUN pip install --no-cache-dir -r requirements.txt

CMD python -m flask run --host=0.0.0.0 --port=8080
