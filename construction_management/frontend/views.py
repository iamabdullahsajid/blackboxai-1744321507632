from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    context = {
        'active_projects_count': 0,
        'active_labourers_count': 0,
        'total_transactions': 0,
        'vendors_count': 0,
    }
    return render(request, 'dashboard.html', context)

@login_required
def vendors_list(request):
    return render(request, 'vendors/list.html', {'vendors': []})

@login_required
def labour_list(request):
    return render(request, 'labour/list.html', {'labourers': []})

@login_required
def transactions_list(request):
    return render(request, 'transactions/list.html', {'transactions': []})

@login_required
def reports_list(request):
    return render(request, 'reports/list.html')
