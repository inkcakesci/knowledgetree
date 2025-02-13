
# django_knowledge_tree

项目名：没想好。

摘要：使用 NoSQL（JSON）方式存储知识点树数据，支持知识点树的编辑、保存、删除，通过前端组件（如 jsTree）将 JSON 数据以图形化树形结构展示。

## 项目结构

```
django_knowledge_tree/
├── Dockerfile
├── manage.py
├── requirements.txt
├── knowledge_tree/          # 主 Django 工程目录
│   ├── __init__.py
│   ├── settings.py          # Django 配置文件
│   ├── urls.py              # 项目级 URL 配置
│   └── wsgi.py              # WSGI 入口
└── tree/                    # 应用目录，包含模型、视图、模板、静态文件等
    ├── __init__.py
    ├── models.py            # 模型定义（知识点树记录）
    ├── forms.py             # Django 表单定义
    ├── views.py             # 视图函数，包括知识点树的创建、编辑、展示、删除等
    ├── urls.py              # 应用级 URL 配置
    ├── templates/
    │   └── tree/
    │       ├── base.html         # 基础模板，包含全局静态资源加载（jQuery、Bootstrap、sb-admin-2 等）
    │       ├── index.html        # 知识点树列表页
    │       ├── edit.html         # 编辑/创建知识点树页面
    │       ├── tree_view.html    # 知识点树展示页（同时显示 JSON 原文和图形化树）
    │       └── confirm_delete.html  # 删除确认页
    └── static/
        ├── css/
        │   └── sb-admin-2.min.css   # 引入 sb-admin-2 的 CSS 文件
        └── js/
            ├── jquery-3.7.1.min.js    # jQuery 脚本
            ├── sb-admin-2.js          # sb-admin-2 调试版脚本（可选）
            └── sb-admin-2.min.js      # sb-admin-2 压缩版脚本

```

## 环境要求

- Python 3.8 及以上
- Django 3.2 及以上

## 安装

1. **克隆代码**

   ```bash
   git clone https://github.com/inkcakesci/knowledgetree.git
   cd django_knowledge_tree
   ```

2. **创建并激活虚拟环境**

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **安装依赖**

   ```bash
   pip install -r requirements.txt
   ```

## 数据库迁移

在项目根目录下执行：

```bash
python manage.py makemigrations
python manage.py migrate
```

## 静态资源
使用 `python manage.py collectstatic` 生成静态文件集合。

## 运行项目

在项目根目录下运行：

```bash
python manage.py runserver
```

浏览器中打开 `http://127.0.0.1:8000/` 即可访问知识点树列表页面。

## Docker 部署

提供了 Dockerfile，可用于构建 Docker 镜像。构建和运行命令示例如下：

```bash
docker build -t django_knowledge_tree .
docker run -p 8000:8000 django_knowledge_tree
```
## 其他

- 基于 sb-admin-2 前端模板进行二次开发，前端样式和布局可根据需要自行修改。
- 如果需要扩展其他功能，例如用户认证、权限管理等，请根据 Django 官方文档进行相应配置。


# 录入格式说明

本项目中的知识点树数据采用符合 jsTree 组件要求的嵌套 JSON 格式。整个 JSON 数据由一个或多个节点组成，每个节点包含以下主要字段：

- **id**：字符串类型，用于唯一标识该节点。通常可以用类似 "node1", "node1_1" 等方式命名，确保在整个树中唯一。
- **text**：字符串类型，表示节点要显示的文本内容。
- **children**：数组类型，包含该节点的子节点。如果该节点没有子节点，可以设为一个空数组或省略此字段。

## Prompt样例1

如果你希望利用 AI（如 ChatGPT、DeepSeek）生成符合上述格式的 JSON，可以使用类似下面的提示语（Prompt）：

```markdown
你是一名专业的教辅资料整理教师，请生成一份符合 jsTree 格式的 JSON 知识点树，要求如下：  
- 根节点名称为 "[科目]"。  
- 根节点下有一个子节点 "[课本名称]"。
- 该子节点下包含多个单元或章节。
- 每个单元下包含详细的知识点内容。请详细搜索相关教材内容，确保内容尽量完整和准确。  
- 请确保生成的 JSON 数据结构符合 jsTree 的嵌套格式，并为每个节点指定唯一的 id。  

现在要求你生成：《XXXXXX》的知识点树，以 JSON 格式返回。  

```
（请在 “XXXXXX” 中填入具体的课本名称，例如 “人教版高中英语必修一 (高一上册)”。）

## Prompt样例2
```markdown
你是一名专业的教辅资料整理教师，请生成一份符合 jsTree 格式的 JSON 知识点树，要求如下：  
- 根节点名称为 "[科目]"。  
- 根节点下有一个子节点 "{年级+上下册}"。
- 该子节点下包含多个单元或章节。
- 每个单元下包含详细的知识点内容。请详细搜索相关教材内容，确保内容尽量完整和准确。  
- 请确保生成的 JSON 数据结构符合 jsTree 的嵌套格式，并为每个节点指定唯一的 id。  
- 参考现有的成熟教辅资料和参考书，如曲一线、王后雄等教辅。
现在要求你生成：《人教版初中日语》的知识点树，以 JSON 格式返回，对于日语这一科目，着重考虑语法点和考点等，请提供完整的从初一到初三的所有课本内容。
```


## changelog

### 2025年2月4日：

修正了一次创建新知识点树会生成2个的逻辑错误。

### 2025年2月10日：
数据库改为使用PostgreSQL
```bash
docker run --name postgres -e POSTGRES_USER=klgtree -e POSTGRES_PASSWORD=klgtree123 -e POSTGRES_DB=knowledge_tree -p 5432:5432 -d postgres
```
# 数据库备份方法：

在 Docker 容器中，`/temp` 目录通常不存在。

**解决方案**：

1. **使用容器内存在的目录**：

   您可以将备份文件输出到容器内已存在的目录，例如 `/tmp`。

   修改您的命令如下：

   ```bash
   docker exec -t postgres pg_dump -U klgtree knowledge_tree -f /tmp/backup.sql
   ```

   这将把备份文件保存到容器内的 `/tmp` 目录。

2. **将备份文件复制到宿主机**：

   备份完成后，您可以使用 `docker cp` 命令将备份文件从容器复制到宿主机：

   ```bash
   docker cp postgres:/tmp/backup.sql /path/to/host/backup.sql
   ```

   请将 `/path/to/host/backup.sql` 替换为您希望在宿主机上保存备份文件的路径。

3. **清理容器内的备份文件**：

   备份完成后，您可以删除容器内的临时备份文件：

   ```bash
   docker exec postgres rm /tmp/backup.sql
   ```
