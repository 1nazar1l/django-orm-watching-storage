from datetime import datetime, timezone


def get_duration(entered_at, leaved_at = None):
    if leaved_at:
        delta = leaved_at - entered_at
    else:
        utc_time = datetime.now(timezone.utc)
        delta = utc_time - entered_at
    
    return delta

def format_duration(delta):
    total_seconds_inside = delta.total_seconds()
    
    hours_inside = int(total_seconds_inside // 3600)
    minutes_inside = int((total_seconds_inside % 3600) // 60)
    second_inside = int(((total_seconds_inside % 3600) % 60) // 60)
    
    return f'{hours_inside}:{minutes_inside}:{second_inside}'