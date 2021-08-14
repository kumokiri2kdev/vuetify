import k2kparser.calendar as pc
import json



if __name__ =='__main__':
    events = {}

    for i in range(1, 13):
        p = pc.ParserCalendar(year=2021, month=i)
        kaisais = p.parse()

        for day in kaisais:
            tag = '{}{:02d}'.format(day['year'], day['month'])
            if tag not in events:
                events[tag] = {}

            day_tag = '{}-{:02d}-{:02d}'.format(day['year'], day['month'], day['day'])
            events[tag][day_tag] = []
            for kaisai in day['races']:
                kaisai_info = {
                    'kaisai': kaisai['kaisai'],
                    'races':  kaisai['races']
                }
                events[tag][day_tag].append(kaisai_info)

    with open('kaisai.json', mode='w') as f:
        json.dump(events,f, indent=4, ensure_ascii=False)
