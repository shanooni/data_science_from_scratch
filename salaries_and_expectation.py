from collections import defaultdict
from data import salaries_and_tenures

salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
# print(salary_by_tenure)

average_salary_by_tenure = {
    tenure : sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two years"
    elif tenure < 5:
        return "between two and five years"
    else:
        return "more than five years"
    
salary_by_tenure_bucket = defaultdict(list)

for salary,tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
# print(salary_by_tenure_bucket)

average_salary_by_bucket = {
    tenure_bucket : sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
# print(average_salary_by_bucket)
# print(average_salary_by_tenure)