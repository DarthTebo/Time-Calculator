

def add_time(start, duration):

    div_start = start.split()
    hours = div_start[0]
    hour, minut = hours.split(":")
    hour = int(hour)
    minut = int(minut)

    zone = div_start[1]

    if zone == "PM":
        hour += 12

    hour_ex, minut_ex = duration.split(":")
    hour_ex = int(hour_ex)
    minut_ex = int(minut_ex)

    total_minutes = minut + minut_ex
    ans_minutes = total_minutes % 60
    extra_hours = total_minutes // 60
    total_hour = hour + hour_ex + extra_hours

    ans_hour = (total_hour % 24) % 12

    if ans_hour == 0:
        ans_hour = 12
    ans_hour = str(ans_hour)

    total_day = (total_hour // 24)

    ans_midday = ""
    if (total_hour % 24) <= 11:
        ans_midday = "AM"
    else:
        ans_midday = "PM"

    if ans_minutes <= 9:
        ans_minutes = '0' + str(ans_minutes)
    else:
        ans_minutes = str(ans_minutes)

    time_stamp = ans_hour + ":" + ans_minutes + ' ' + ans_midday

    if total_day == 0:
        return time_stamp
    if total_day == 1:
        return time_stamp + ' (next day)'

    return time_stamp + ' (' + str(total_day) + ' days later)'



    
