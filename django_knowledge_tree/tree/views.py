from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import KnowledgeTree
from .forms import KnowledgeTreeForm
import json

def index(request):
    # 获取第一条记录，不存在则创建一个空记录
    tree_instance = KnowledgeTree.objects.first()
    if tree_instance is None:
        tree_instance = KnowledgeTree.objects.create(data={})
    context = {'tree': json.dumps(tree_instance.data, indent=4, ensure_ascii=False)}
    return render(request, 'tree/index.html', context)

def edit_tree(request):
    tree_instance = KnowledgeTree.objects.first()
    if tree_instance is None:
        tree_instance = KnowledgeTree.objects.create(data={})
    if request.method == 'POST':
        form = KnowledgeTreeForm(request.POST, instance=tree_instance)
        if form.is_valid():
            form.save()
            return redirect('tree:index')
    else:
        form = KnowledgeTreeForm(instance=tree_instance)
    return render(request, 'tree/edit.html', {'form': form})

# API 接口：支持 AI prompt 直接传入 JSON 更新知识树数据
def update_tree_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': '无效的 JSON 数据'}, status=400)
        tree_instance = KnowledgeTree.objects.first()
        if tree_instance is None:
            tree_instance = KnowledgeTree.objects.create(data=data)
        else:
            tree_instance.data = data
            tree_instance.save()
        return JsonResponse({'message': '知识树更新成功'})
    return JsonResponse({'error': '仅支持 POST 请求'}, status=405)
