FROM python:3.9-alpine
WORKDIR /relabs_adsspot_bot
COPY ./ /relabs_adsspot_bot
RUN apk update && pip install -r /relabs_adsspot_bot/requirements.txt --no-cache-dir
ADD https://github.com/Careprop/relabs_adsspot_bot
CMD ["python", "main.py"]