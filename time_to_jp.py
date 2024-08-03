from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_time_difference(target_date_str):
    # Parse the input date string
    target_date = datetime.strptime(target_date_str, '%Y-%m-%d %H:%M:%S')
    
    # Get the current date and time
    now = datetime.now()
    
    # Calculate the difference
    delta = relativedelta(target_date, now)
    
    # Calculate total seconds difference
    total_seconds = (target_date - now).total_seconds()
    
    # Calculate total hours difference
    total_hours = total_seconds // 3600
    
    # Calculate total days difference
    total_days = total_seconds // (3600 * 24)
    
    # Calculate total weeks difference
    total_weeks = total_days // 7
    
    # Calculate total months difference
    total_months = delta.years * 12 + delta.months
    
    print(f"Time difference from now to {target_date_str}:")
    print(f"Years: {delta.years}")
    print(f"Months: {total_months}")
    print(f"Weeks: {total_weeks}")
    print(f"Days: {total_days}")
    print(f"Hours: {total_hours}")
    print(f"Seconds: {total_seconds}")

if __name__ == "__main__":
    target_date_str = input("Enter the target date (YYYY-MM-DD HH:MM:SS): ")
    calculate_time_difference(target_date_str)