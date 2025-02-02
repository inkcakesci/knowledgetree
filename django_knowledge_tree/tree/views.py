from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import KnowledgeTree
from .forms import KnowledgeTreeForm
import json

def index(request):
    # 列出所有的知识点树
    trees = KnowledgeTree.objects.all()
    return render(request, 'tree/index.html', {'trees': trees})

def view_tree(request, tree_id):
    tree_instance = get_object_or_404(KnowledgeTree, id=tree_id)
    # 将 data 字段序列化为 JSON 字符串
    tree_json_str = json.dumps(tree_instance.data, ensure_ascii=False)
    return render(request, 'tree/tree_view.html', {
        'tree': tree_instance,
        'tree_json_str': tree_json_str  # 注意这里传递的是字符串
    })

def edit_tree(request, tree_id=None):
    if tree_id:
        tree_instance = get_object_or_404(KnowledgeTree, id=tree_id)
    else:
        # 如果未提供 id，则创建新记录
        tree_instance = KnowledgeTree.objects.create(title="新知识点树", data={})
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