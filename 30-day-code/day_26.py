def compute_fine(return_data, issue_data):
    return_date, return_month, return_year = [int(item) for item in return_data]
    issue_date, issue_month, issue_year = [int(item) for item in issue_data]
    if issue_year == return_year:
        if issue_month == return_month:
            return 15 * max(return_date - issue_date, 0)
        elif return_month > issue_month:
            return 500 * (return_month - issue_month)
    elif return_year > issue_year:
        return 10_000
    return 0


print(compute_fine(
    input().split(), input().split()
))
