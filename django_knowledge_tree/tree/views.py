from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import KnowledgeTree
from .forms import KnowledgeTreeForm
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistrationForm
def index(request):
    # 列出所有的知识点树
    trees = KnowledgeTree.objects.all()
    return render(request, 'tree/index.html', {'trees': trees})

def add_keywords(node):
    """
    给每个节点添加关键字字段，若没有关键字字段时，防止报错。
    """
    # 检查节点是否有关键字，如果没有就添加一个空列表
    if 'keywords' not in node:
        node['keywords'] = []
    
    # 递归处理子节点
    if 'children' in node:
        for child in node['children']:
            add_keywords(child)

def view_tree(request, tree_id):
    tree_instance = get_object_or_404(KnowledgeTree, id=tree_id)
    tree_data = tree_instance.data
    
    # 为每个节点添加关键字字段
    add_keywords(tree_data)
    
    tree_json_str = json.dumps(tree_data, ensure_ascii=False)
    
    return render(request, 'tree/tree_view.html', {
        'tree': tree_instance,
        'tree_json_str': tree_json_str  # 注意这里传递的是字符串
    })

@login_required
def edit_tree(request, tree_id=None):
    if tree_id:
        tree_instance = get_object_or_404(KnowledgeTree, id=tree_id)
    else:
        # 如果没有 tree_id，才创建新的知识点树
        tree_instance, created = KnowledgeTree.objects.get_or_create(title="新知识点树")
        # 这里的 get_or_create 确保只创建一个新的知识点树，避免重复插入
        # 如果已有相同标题的知识点树，直接获取
    if request.method == 'POST':
        form = KnowledgeTreeForm(request.POST, instance=tree_instance)
        if form.is_valid():
            form.save()
            return redirect('tree:index')
    else:
        form = KnowledgeTreeForm(instance=tree_instance)
    return render(request, 'tree/edit.html', {
        'form': form,
        'tree_id': tree_instance.id
    })

@login_required
def delete_tree(request, tree_id):
    tree_instance = get_object_or_404(KnowledgeTree, id=tree_id)
    if request.method == 'POST':
        tree_instance.delete()
        return redirect('tree:index')
    return render(request, 'tree/confirm_delete.html', {'tree': tree_instance})

def update_tree_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': '无效的 JSON 数据'}, status=400)
        tree_instance = KnowledgeTree.objects.first()
        if tree_instance is None:
            tree_instance = KnowledgeTree.objects.create(title="自动更新知识树", data=data)
        else:
            tree_instance.data = data
            tree_instance.save()
        return JsonResponse({'message': '知识树更新成功'})
    return JsonResponse({'error': '仅支持 POST 请求'}, status=405)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 自动登录新用户
            return redirect('tree:index')
    else:
        form = RegistrationForm()
    return render(request, 'tree/register.html', {'form': form})