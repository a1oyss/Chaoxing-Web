FROM python:3.7

COPY . .
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]