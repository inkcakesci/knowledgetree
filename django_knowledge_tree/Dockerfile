FROM python:3.9-slim

# 防止生成 pyc 文件
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# 安装依赖
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 复制代码
COPY . /app/

# 收集静态文件
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "knowledge_tree.wsgi:application", "--bind", "0.0.0.0:8000"]
