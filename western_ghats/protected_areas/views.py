from django.shortcuts import render
from .models import ProtectedArea

def protected_area_list(request):
    queryset = ProtectedArea.objects.all()

    # Filter by category
    category = request.GET.get('category')
    if category:
        queryset = queryset.filter(category=category)

    # Filter by state
    state = request.GET.get('state')
    if state:
        queryset = queryset.filter(state=state)

    # Get unique states for filter dropdown
    states = ProtectedArea.objects.values_list('state', flat=True).distinct()

    context = {
        'protected_areas': queryset,
        'states': states,
        'selected_category': category,
        'selected_state': state,
        'categories': ProtectedArea.CATEGORY_CHOICES,
    }
    return render(request, 'protected_areas/home.html', context)


def protected_area_detail(request, pk):
    protected_area = ProtectedArea.objects.get(pk=pk)
    context = {
        'protected_area': protected_area
    }
    return render(request, 'protected_areas/deatils.html', context)