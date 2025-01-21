from datetime import datetime, date, time, timedelta

date1 = input("Enter start date in (YYYY-MM-DD) Format:")
date2 = input("Enter end date in (YYYY-MM-DD) Format:")

all_days = []
all_task = []

try:
    start_date = datetime.strptime(date1, "%Y-%m-%d")
    end_date = datetime.strptime(date2, "%Y-%m-%d")
    if start_date > end_date:
        print("Start Date should be less than End date.")
    else:
        days_diff = (end_date - start_date).days
        for i in range(days_diff + 1):
            current_date = start_date + timedelta(days=i)
            check_day = current_date.strftime("%A")
            if check_day not in ["Saturday", "Sunday"]:

                all_days.append(current_date.strftime("%Y-%m-%d, %A"))
                task = input(f"Enter task {current_date.strftime('%A, %d-%m-%Y')}")
                all_task.append(task)
            else:
                print(
                    f"{current_date.strftime('%Y-%m-%d')} because of {current_date.strftime('%A')} task not assigned."
                )

        print(dict(zip(all_days, all_task)))

except ValueError:
    print("Date format is not correct")
