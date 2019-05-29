import json

json_retezec = """
    {
      "jméno": "Anna",
      "město": "Brno",
      "jazyky": ["čeština", "angličtina", "Python"],
      "věk": 26
    }
"""
print(json_retezec)
data = json.loads(json_retezec)
print(data)
print(data['město'])

print(json.dumps(data,ensure_ascii=False, indent=2))