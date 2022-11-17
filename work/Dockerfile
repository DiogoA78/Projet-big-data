FROM python:3.8


# copy files
COPY ../requirements.txt ./

RUN pip3 install -r requirements.txt

CMD ["streamlit","run", "streamlit_app.py"]