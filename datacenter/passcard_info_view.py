from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from tools import get_duration, format_duration


def is_visit_long(delta):
        total_seconds = delta.total_seconds()
        hours_inside = total_seconds // 3600
        result = hours_inside >= 1
        return result

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcards_visits = Visit.objects.filter(passcard = passcard)
    this_passcard_visits  = []
    
    for passcard_visit in passcards_visits:
        
        leaved_at = passcard_visit.leaved_at
        entered_at = passcard_visit.entered_at
        
        time_inside_bank = get_duration(entered_at, leaved_at)
        suspicious_visit = is_visit_long(time_inside_bank)
        formatted_time_inside = format_duration(time_inside_bank)
        
        this_passcard_visits.append(
            {
                'entered_at': entered_at,
                'duration': formatted_time_inside,
                'is_strange': suspicious_visit
            })
        
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    
    return render(request, 'passcard_info.html', context)
