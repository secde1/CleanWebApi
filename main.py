import requests
import json

params = {
    'models': 'nudity-2.0,gore',
    'api_user': '1874164527',
    'api_secret': 'CsuXLBMCbSLgK6JYpDzdoWbSckQ4RjUv'
}

# pornographic
# normal

files = {'media': open('normal.jpg', 'rb')}
r = requests.post('https://api.sightengine.com/1.0/check.json', files=files, data=params)
output = json.loads(r.text)

if 'nudity' in output:
    nudity_data = output['nudity']
    suggestive = nudity_data.get('suggestive', 0)
    if suggestive > 0.5:
        pass
        print("Изображение может содержать суггестивный контент и требует дополнительной проверки.")
    else:
        pass
        print("Изображение безопасно.")
else:
    print("Информация о наготе отсутствует в ответе API.")
if 'nudity' in output:
    nudity_data = output['nudity']
    suggestive = nudity_data.get('suggestive', 0)
    sexual_activity = nudity_data.get('sexual_activity', 0)
    erotica = nudity_data.get('erotica', 0)
    sexual_display = nudity_data.get('sexual_display', 0)

    if suggestive > 0.5 or sexual_activity > 0.1 or erotica > 0.2 or sexual_display > 0.5:
        print("Изображение может содержать неприемлемый контент и требует ручной проверки.")
    else:
        print("Изображение безопасно.")
else:
    print("Информация о наготе отсутствует в ответе API.")

print(json.dumps(output, indent=4))

files['media'].close()
