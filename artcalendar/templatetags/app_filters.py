from django import template

register = template.Library()

@register.filter(is_safe=True, name='opening_datetime')
def opening_datetime(event):
    """ Return a nicely formatted opening date and time """
    dt = "%s, %s-%s" % (event.opening_date.strftime('%A, %B %e'),
        event.opening_start_time.strftime('%l:%M'), event.opening_end_time.strftime('%l:%M %p'))
    dt = dt.replace(':00', '')
    dt = dt.replace('  ', ' ')
    dt = dt.replace('- ', '-')
    return dt
