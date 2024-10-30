consultants = [
    {"name": "Peyton Turner", "company": "Walker Inc"},
    {"name": "Isaias Fritsch", "company": "Walker Inc"},
    {"name": "Susana Wilderman", "company": "Nolan Inc"}
]

grouped_by_company = {}

for consultant in consultants:
    company = consultant["company"]
    if company not in grouped_by_company:
        grouped_by_company[company] = []
    grouped_by_company[company].append(consultant)

print(grouped_by_company)
