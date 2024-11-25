from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from custom_user.models import CustomUser
from django.contrib import messages

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def task_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            user = request.user
            task = Task.objects.filter(assign_to=user)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Task Created'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_task(request, pk= None):
    # id = pk 
    user = request.user
    # task = Task.objects.filter(assign_to=user)
    task = Task.objects.get(pk=pk)
    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
    elif request.method == 'PATCH':
        serializer = TaskSerializer(task, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response({'msg': 'Task Update'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, pk=None):
    user = request.user
    task = Task.objects.get(pk=pk)
    task.delete()
    return Response({'msg': 'Task Deleted'}, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
def mark_task_completed(request, pk):
    task = Task.objects.get(pk)
    if task.assign_to != request.user:
          return Response({"error": "You do not have permission to update this task."}, status=status.HTTP_403_FORBIDDEN)
    task.status = 'Completed'
    task.save()
    return Response({"message": "Task marked as completed"}, status=status.HTTP_200_OK)











    # if request.method == 'PUT':
    #     id = pk
    #     task =Task.objects.get(id=id)
    #     serializer = TaskSerializer(task, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'Task Update'}, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # if request.method == 'PATCH':
    #     id = pk
    #     task = Task.objects.get(id=id)
    #     serializer = TaskSerializer(task, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg': 'Task Update'}, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # if request.method == 'DELETE':
    #     id = pk
    #     task = Task.objects.get(id=id)
    #     task.delete()
    #     return Response({'msg': 'Task Deleted'}, status=status.HTTP_200_OK)
    


def add_task(request):
    user= CustomUser.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        duedate = request.POST.get('due_date')
        status = request.POST.get('status')
        assign_to = request.POST.get('assign_to')

        Task.objects.create(title=title, description=description, due_date=duedate, status=status, assign_to_id=assign_to)
        messages.success(request, "Task assigned success")
        return redirect('task_list')
    return render(request, 'task.html' , {'user': user})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
