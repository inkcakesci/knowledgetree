# 使用 Python 3.9-slim 作为基础镜像
FROM python:3.9-slim

# 禁止生成 .pyc 文件，并确保日志实时输出
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 设置工作目录
WORKDIR /app

# 复制依赖配置文件并安装依赖
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# 复制整个项目到容器中
COPY . /app/

# 收集静态文件（如果需要）
RUN python manage.py collectstatic --noinput

# 暴露端口 8000
EXPOSE 8000

# 启动 gunicorn 作为 WSGI 服务器
CMD ["gunicorn", "knowledge_tree.wsgi:application", "--bind", "0.0.0.0:8000"]
