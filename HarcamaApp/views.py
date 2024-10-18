import json
import xml.etree.ElementTree as ET
from datetime import timezone
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.http import HttpResponse
from django.utils import timezone
import pytz
from django.contrib.sessions.models import Session


def zaman(request):
    print(f"Current time: {timezone.now()}")
    print(f"Current timezone: {timezone.get_current_timezone()}")
    print(f"All timezones: {pytz.all_timezones}")
    # ... rest of your view code


@login_required
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.timestamp = timezone.now()
            expense.save()
            messages.success(request, 'Bilgiler başarıyla kaydedildi.')
            # Create JSON
            expense_data = {
                'timestamp': expense.timestamp.isoformat(),
                'kalem': expense.kalem,
                'kart': expense.kart,
                'fiyat': str(expense.fiyat),
                'bilgi': str(expense.bilgi),
                'user': expense.user.username
            }
            json_data = json.dumps(expense_data, ensure_ascii=False, indent=2)

            # Create XML
            root = ET.Element('expense')
            for key, value in expense_data.items():
                child = ET.SubElement(root, key)
                child.text = value
            xml_data = ET.tostring(root, encoding='unicode', method='xml')

            # Here you would add the Google Drive upload logic
            #            messages.success(request, 'Harcama başarıyla kaydedildi.')
            return redirect('expense_create')
        else:
            messages.error(request, f'Form geçerli değil. Hatalar: {form.errors}')
    else:
        form = ExpenseForm()

    # Fetch the 5 most recent expenses for the current user
    expenses = Expense.objects.filter(user=request.user).order_by('-timestamp')[:5]
    return render(request, 'expenses/expense_form.html', {'form': form, 'expenses': expenses})


#     # Debug: Print the SQL query
#     print(expenses.query)
#
#     # Debug: Print expense details
#     for expense in expenses:
#         print(f"Expense ID: {expense.id}, Timestamp: {expense.timestamp}, Amount: {expense.fiyat}")
#
#     return render(request, 'expenses/expense_form.html', {'form': form, 'expenses': expenses})
#
#
# # Add this function to your views.py for debugging
# def debug_expenses(request):
#     if request.user.is_authenticated:
#         expenses = Expense.objects.filter(user=request.user).order_by('-timestamp')[:10]
#     else:
#         expenses = Expense.objects.none()
#     return render(request, 'expenses/debug_expenses.html', {'expenses': expenses})


def custom_logout(request):
    if request.user.is_authenticated:
        # Delete all sessions for this user
        Session.objects.filter(session_data__contains=str(request.user.id)).delete()
    logout(request)
    request.session.flush()
    messages.success(request, 'Başarıyla sistemden çıkılmıştır.')
    return redirect('giris')


def current_time(request):
    now = timezone.now()
    html = f"<html><body>It is now {now} in the server's time.</body></html>"
    return HttpResponse(html)
