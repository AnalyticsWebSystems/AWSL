from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Representative, Message, Conversation
from django.contrib import messages
from .forms import MessageForm


# Create your views here.
@login_required
def choose_representative(request):
    representatives = Representative.objects.all()
    return render(request, 'chat/choose_representative.html', {'representatives': representatives})


@login_required
def send_message(request, representative_id):
    representative = Representative.objects.get(id=representative_id)
    conversation = Conversation.objects.filter(user=request.user, representative=representative).first()
    if not conversation:
        conversation = Conversation.objects.create(user=request.user, representative=representative)

    all_messages = Message.objects.filter(conversation=conversation).order_by('timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Message.objects.create(conversation=conversation, sender=request.user, content=content)
            messages.success(request, "Your message has been delivered")
            return redirect('chat:conversation_detail', representative_id=representative_id)
    else:
        form = MessageForm()

    return render(request, "chat/conversation_detail.html", {
        "representative": representative,
        "all_messages": all_messages,
        "form": form,
    })


# def send_message(request, representative_id):
#     if request.method == 'POST':
#         content = request.POST.get('content')
#         sender = request.user
#         representative = Representative.objects.get(id=representative_id)
#         Message.objects.create(sender=sender, recipient=representative, content=content)
#         messages.success(request, "Your message has been delivered")
#         return redirect('app:index')
#     return render(request, "chat/conversation_detail.html", {
#         # "representative": representative,
#     })


# views.py

@login_required
def conversation_detail(request, representative_id):
    representative = Representative.objects.get(id=representative_id)
    conversation, created = Conversation.objects.get_or_create(user=request.user, representative=representative)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Message.objects.create(conversation=conversation, sender=request.user, content=content)
            messages.success(request, "Your message has been delivered")
            return redirect('chat:conversation_detail', representative_id=representative_id)
    else:
        form = MessageForm()
    return render(request, 'chat/conversation_detail.html', {
        'conversation': conversation,
        'representative': representative,
        'form': form,
    })


@login_required
def inbox(request):
    representatives = Representative.objects.all()
    conversations = Conversation.objects.filter(user=request.user)
    return render(request, 'chat/inbox.html', {
        'conversations': conversations,
        'representatives': representatives,
    })
