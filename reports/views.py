from django.shortcuts import render
from animals.models import Animal
from django.core.paginator import Paginator


def reports_view(request):
    animals = Animal.objects.filter(is_found=False)
    paginator = Paginator(animals, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'reports/reports.html', {'page_obj': page_obj})


def report_details(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'reports/report_details.html', {'animal': animal})
