#!/usr/bin/env python3
import json, urllib.request

URL = "https://api.brandmeister.network/v2/talkgroup"

def main():
    with urllib.request.urlopen(URL) as resp:
        data = json.loads(resp.read())

    # Оставляем только TG, начинающиеся с '250', и сортируем их
    sorted_ids = sorted((tg_id for tg_id in data if tg_id.startswith('250')), key=int)

    with open('tg.txt', 'w', encoding='utf-8') as f:
        for tg_id in sorted_ids:
            name = data[tg_id]
            if 'Caucasus' in name:
                name = name.replace('Caucasus',
                    'Kavkaz /YSF/D-Star/NXDN/Wires/P25/FM')
            f.write(f"TG  {tg_id:<7} {name}\n")

    print(f"Saved {len(sorted_ids)} talkgroups to tg.txt")

if __name__ == "__main__":
    main()
