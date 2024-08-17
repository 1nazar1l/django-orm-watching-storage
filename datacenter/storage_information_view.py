from datacenter.models import Visit
from django.shortcuts import render
from tools import get_duration, format_duration


def storage_information_view(request):
    not_leaved_passcards = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    
    for passcard in not_leaved_passcards:
        entered_at = passcard.entered_at
        
        time_inside_bank = get_duration(entered_at)
        formatted_time_inside = format_duration(time_inside_bank)
        
        non_closed_visits = [
            {
                'who_entered': passcard.passcard.owner_name,
                'entered_at': entered_at,
                'duration': formatted_time_inside,
            }
        ]
        
    context = {
        'non_closed_visits': non_closed_visits, 
    }
    
    return render(request, 'storage_information.html', context)
