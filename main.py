одна_секунда = 1
одна_минута = 60
один_час = 3600
один_день = 86400
одна_неделя = 604800
один_месяц = 2629743
один_год = 31556926
duration = int(input('Укажите время в секундах: '))
if duration < одна_минута:
    print('{} сек'.format(duration))
elif одна_минута <= duration and один_час > duration:
    минута = (duration // одна_минута)
    секунда = (duration % одна_минута)
    print('{} мин {} сек'.format(минута, секунда));
elif duration >= один_час and duration < один_день:
    час = (duration // один_час)
    duration = (duration % один_час)
    минута  = (duration // одна_минута)
    секунда = (duration % одна_минута)
    print('{} час {} мин {} сек'.format(час, минута, секунда));
elif duration >= один_день and duration < одна_неделя:
    день = (duration // один_день)
    duration = (duration % один_день)
    час = (duration // один_час)
    duration = (duration % один_час)
    минута = (duration // одна_минута)
    секунда = (duration % одна_минута)
    print('{} день {} час {} мин {} сек'.format(день, час, минута, секунда));
elif duration >= одна_неделя and duration < один_месяц:
    неделя = (duration // одна_неделя)
    duration = (duration % одна_неделя)
    день = (duration // один_день)
    duration = (duration % один_день)
    час = (duration // один_час)
    duration = (duration % один_час)
    минута = (duration // одна_минута)
    секунда = (duration % одна_минута)
    print('{} нед {} дн {} час {} мин {} сек'.format(неделя, день, час, минута, секунда));
elif duration >= один_месяц and duration < один_год:
    месяц = (duration // один_месяц)
    duration = (duration % один_месяц)
    неделя = (duration // одна_неделя)
    duration = (duration % одна_неделя)
    день = (duration // один_день)
    duration = (duration % один_день)
    час = (duration // один_час)
    duration = (duration % один_час)
    минута = (duration // одна_минута)
    секунда = (duration % одна_минута)
    print('{} мес {} нед {} дн {} час {} мин {} сек'.format(месяц, неделя, день, час, минута, секунда));
