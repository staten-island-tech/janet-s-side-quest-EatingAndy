membership_plan = {
    "Basic": {"monthly fee": 20, "min_duration": 3, "service": []},
    "Premium": {"monthly fee": 40, "min_duration": 6, "service": ["personal_trainer", "spa access"] }
}
plan = input()
duration = int(input())
service = input().split(',')
def membership():
    for key, value in membership_plan.items():
        if key == plan:
            monthlyfee = value["monthly fee"]
            minduration = value["min_duration"]
            break
    if duration <= minduration:
            duration == minduration
    else:
            duration == duration
    totalcost = monthlyfee * duration
    print(f"Total cost before discounts: ${totalcost}")
    if len(service) >= 2:  
            totalcost *= 0.93
    if duration >= 12: 
            totalcost *= 0.9 
    print(f"Total cost after discounts: ${totalcost}")             
membership()