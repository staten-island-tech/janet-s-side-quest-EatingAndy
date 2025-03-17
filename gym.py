membership_plan = {
    "Basic": {"monthly fee": 20, "min_duration": 3, "service": []},
    "Premium": {"monthly fee": 40, "min_duration": 6, "service": ["personal_trainer", "spa access"] }
}
plan = input()
duration = int(input())
service = input()

""" def membership():
    if plan in membership_plan:
        for key, value in membership_plan[plan].items():
            print(key, value)
    else:
        print("Invalid plan.")

membership()
         """

""" def membership():
    if plan in membership_plan:
        for key, value in membership_plan[plan].items():
            if duration <= value:
                value = value
            else:
                value = duration
            print(key, value)
membership() """

membership_plan = {
    "Basic": {"monthly fee": 20, "min_duration": 3, "service": []},
    "Premium": {"monthly fee": 40, "min_duration": 6, "service": ["personal_trainer", "spa access"]}
}

plan = input()
duration = int(input())
service = input()

def membership():
    if plan in membership_plan:
        for key, value in membership_plan[plan].items():
            if key == "monthly fee":
                total_cost = value * max(duration, membership_plan[plan]["min_duration"])
                print(f"{key}: {value}, Total Cost: {total_cost}")
            elif key == "service":
                if service in value:
                    print(f"Additional Service: {service}")
                else:
                    print(f"Service '{service}' is not available for the {plan} plan.")
            else:
                print(f"{key}: {value}")
    else:
        print("Invalid plan.")
