


def filtering(events):
    filtered_events = {}

    for k, v in events.items():
        filtered_kaisais = []
        for kaisai in v:
            filtered_races = []
            for race in kaisai['races']:
                if race['class'].startswith('2歳'):
                    filtered_races.append(race)
            if len(filtered_races) > 0:
                kaisai['races'] = filtered_races
                filtered_kaisais.append(kaisai)

        if len(filtered_kaisais) > 0:
            filtered_events[k] = filtered_kaisais

    return filtered_events

    
