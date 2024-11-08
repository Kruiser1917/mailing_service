from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Message, Mailing
from .forms import ClientForm, MessageForm, MailingForm
from django.contrib import messages
from django.http import JsonResponse

def send_mailing(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    # Логика отправки (здесь упрощенно)
    if mailing.status == 'created':
        mailing.status = 'launched'
        mailing.save()
        return JsonResponse({'success': True, 'message': 'Mailing sent successfully!'})
    return JsonResponse({'success': False, 'message': 'Mailing is not in a valid state.'})

def home(request):
    total_mailings = Mailing.objects.count()  # Общее количество рассылок
    active_mailings = Mailing.objects.filter(status='launched').count()  # Активные рассылки
    unique_clients = Client.objects.count()  # Уникальные получатели

    context = {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'unique_clients': unique_clients,
    }
    return render(request, 'home.html', context)

def create_mailing(request):
    return render(request, 'create_mailing.html')

def mailing_list(request):
    mailings = Mailing.objects.filter(owner=request.user)
    return render(request, 'mailing_list.html', {'mailings': mailings})


@login_required
def client_list(request):
    clients = Client.objects.filter(owner=request.user)  # Фильтруем только свои клиенты
    return render(request, 'client_list.html', {'clients': clients})

@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.owner = request.user  # Устанавливаем текущего пользователя как владельца
            client.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})


@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk, owner=request.user)  # Проверяем владельца
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})


@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk, owner=request.user)  # Проверяем владельца
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'client_confirm_delete.html', {'client': client})

@login_required
def mailing_list(request):
    mailings = Mailing.objects.filter(owner=request.user)
    return render(request, 'mailing_list.html', {'mailings': mailings})


@login_required
def mailing_create(request):
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            mailing = form.save(commit=False)
            mailing.owner = request.user
            mailing.save()
            return redirect('mailing_list')
    else:
        form = MailingForm()
    return render(request, 'mailing_form.html', {'form': form})


@login_required
def mailing_edit(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = MailingForm(request.POST, instance=mailing)
        if form.is_valid():
            form.save()
            return redirect('mailing_list')
    else:
        form = MailingForm(instance=mailing)
    return render(request, 'mailing_form.html', {'form': form})


@login_required
def mailing_delete(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk, owner=request.user)
    if request.method == 'POST':
        mailing.delete()
        return redirect('mailing_list')
    return render(request, 'mailing_confirm_delete.html', {'mailing': mailing})


@login_required
def message_list(request):
    messages = Message.objects.filter(owner=request.user)
    return render(request, 'message_list.html', {'messages': messages})


@login_required
def message_create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.owner = request.user
            message.save()
            return redirect('message_list')
    else:
        form = MessageForm()
    return render(request, 'message_form.html', {'form': form})


@login_required
def message_edit(request, pk):
    message = get_object_or_404(Message, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('message_list')
    else:
        form = MessageForm(instance=message)
    return render(request, 'message_form.html', {'form': form})


@login_required
def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk, owner=request.user)
    if request.method == 'POST':
        message.delete()
        return redirect('message_list')
    return render(request, 'message_confirm_delete.html', {'message': message})
