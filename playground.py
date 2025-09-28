import calendar
import datetime as dt
from decimal import Decimal, ROUND_HALF_UP


# def calculate_refund(plan_type, start_date, cancel_date):
#     syear, smonth, sday = [int(i) for i in start_date.split("-")]
#     cyear, cmonth, cday = [int(i) for i in cancel_date.split("-")]
#
#     start = dt.date(syear, smonth, sday)
#     cancel = dt.date(cyear, cmonth, cday)
#
#     days_used = (cancel - start).days
#
#     if plan_type == "yearly":
#         refund = Decimal(120 / 365) * Decimal(365 - days_used)
#     else:
#         month_length = calendar.monthrange(syear, smonth)[1]
#         refund = Decimal(12 / month_length) * Decimal(month_length - min(days_used, month_length))
#
#     return Decimal(refund).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
#
#
#
#
# print(calculate_refund(plan_type="monthly",
#     start_date="2025-03-01",
#     cancel_date="2025-04-15"))


# def calculate_refund(plan_amount, start_date, cancel_date):
#     # syear, smonth, sday = [int(val) for val in start_date.split('-')]
#     cyear, cmonth, cday = [int(val) for val in cancel_date.split('-')]
#
#     # days_used = Decimal((dt.date(cyear, cmonth, cday) - dt.date(syear, smonth, sday)).days + 1) # +1 to include cancellation date
#     #
#     # smonth_length = Decimal(calendar.monthrange(syear, smonth)[1])
#     cmonth_length = Decimal(calendar.monthrange(cyear, cmonth)[1])
#     daily_rate = Decimal(plan_amount) / cmonth_length
#     days_unused = Decimal(cmonth_length - cday)
#
#     refund_amount = days_unused * daily_rate
#
#     return refund_amount
#
# print(calculate_refund(100, "2015-03-01", "2015-04-20"))
#
# # march 1 - april 20  this is 51 days used
# # april would have 10 days remaining
# # month_length would be 31 from March


# def prorated_charge(monthly_amount, start_date, end_date):
#     start = dt.datetime.strptime(start_date, "%Y-%m-%d").date()
#     end = dt.datetime.strptime(end_date, "%Y-%m-%d").date()
#
#     days_in_month = (end.replace(day=28) + dt.timedelta(days=4)).day
#     daily_rate = Decimal(monthly_amount) / Decimal(days_in_month)
#
#     used_days = (end - start).days
#     return used_days * daily_rate
#
# print(prorated_charge(300, "2025-09-10", "2025-09-20"))

# def generate_invoice(services):
#     invoice = []
#     grand_total = Decimal("0.00")
#     for receipt in services:
#         name = receipt['name']
#         monthly_amount = Decimal(receipt['monthly_amount'])
#         start_date = dt.date(*[int(i) for i in receipt['start_date'].split('-')])
#         cancel_date = dt.date(*[int(i) for i in receipt['cancel_date'].split('-')])
#         service_total = Decimal("0.00")
#         current_date = start_date
#
#         while current_date <= cancel_date:
#             year, month = current_date.year, current_date.month
#             month_length = calendar.monthrange(year, month)[1]
#
#             last_day_of_this_month = dt.date(year, month, month_length)
#             pay_period_end = min(cancel_date, last_day_of_this_month)
#             days_used = Decimal((pay_period_end - current_date).days + 1)
#
#             daily_rate = monthly_amount / Decimal(month_length)
#             month_total = (daily_rate * days_used).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
#
#             service_total += month_total
#             current_date = pay_period_end + dt.timedelta(days=1)
#
#         service_total = service_total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
#         grand_total += service_total
#
#         invoice.append({"service_name": name,
#                         "prorated_amount": float(service_total)})
#
#     invoice.append({"grand_total": float(grand_total)})
#
#     return invoice
#
#
#
#
#
#
#
# services = [
#     {"name": "Service A", "monthly_amount": 120, "start_date": "2025-09-05", "cancel_date": "2025-09-20"},
#     {"name": "Service B", "monthly_amount": 60,  "start_date": "2025-09-01", "cancel_date": "2025-09-30"},
#     {"name": "Service C", "monthly_amount": 90,  "start_date": "2025-09-15", "cancel_date": "2025-09-15"},
# ]
# print(generate_invoice(services))

import datetime as dt
import calendar
from decimal import Decimal


def monthly_charge(month, subscription, users):
    """ Computes the monthly charge for a given subscription.

    @rtype: int
    @returns: the total monthly bill for the customer in cents, rounded
      to the nearest cent. For example, a bill of $20.00 should return 2000.
      If there are no active users or the subscription is None, returns 0.

    @type month: str
    @param month - Always present
      Has the following structure:
      "2022-04"  # April 2022 in YYYY-MM format

    @type subscription: dict
    @param subscription - May be None
      If present, has the following structure:
      {
        'id': 763,
        'customer_id': 328,
        'monthly_price_in_cents': 359  # price per active user per month
      }

    @type users: list
    @param users - May be empty, but not None
      Has the following structure:
      [
        {
          'id': 1,
          'name': "Employee #1",
          'customer_id': 1,

          # when this user started
          'activated_on': datetime.date(2021, 11, 4),

          # last day to bill for user
          # should bill up to and including this date
          # since user had some access on this date
          'deactivated_on': datetime.date(2022, 4, 10)
        },
        {
          'id': 2,
          'name': "Employee #2",
          'customer_id': 1,

          # when this user started
          'activated_on': datetime.date(2021, 12, 4),

          # hasn't been deactivated yet
          'deactivated_on': None
        },
      ]
    """
    # your code here!
    if subscription is None or len(users) == 0:
        return 0

    # We only care about the deactivated month?
    # Calculate daily rate for entire month

    date = month.split('-')
    year, month, day = int(date[0]), int(date[1]), 1
    month_with_day = dt.date(year, month, day)
    plan_rate = Decimal(subscription["monthly_price_in_cents"])
    month_length = calendar.monthrange(year, month)[1]
    daily_rate = plan_rate / Decimal(month_length)  # Maybe not needed to cast the month
    total_active_days = 0

    # Loop through users and accumulate the total days active in the month
    for user in users:
        start_date = user["activated_on"]
        end_date = user["deactivated_on"]
        current_date = month_with_day

        # Determine if a user is active in that month
        if not start_date <= month_with_day:
            continue

        if end_date is not None and end_date <= month_with_day:
            continue

        # Determine how many days that user is active in that month
        while current_date <= last_day_of_month(month_with_day) and end_date:
            total_active_days += 1
            current_date = next_day(current_date)

    print(total_active_days)


####################
# Helper functions #
####################

def first_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the first day of that month. For example:

    >>> first_day_of_month(dt.date(2022, 3, 17))  # Mar 17
    datetime.date(2022, 3, 1)                           # Mar  1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date.replace(day=1)


def last_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the last day of that month. For example:

    >>> last_day_of_month(dt.date(2022, 3, 17))  # Mar 17
    datetime.date(2022, 3, 31)                         # Mar 31

    Input type: datetime.date
    Output type: datetime.date
    """
    last_day = calendar.monthrange(date.year, date.month)[1]
    return date.replace(day=last_day)


def next_day(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the next day. For example:

    >>> next_day(dt.date(2022, 3, 17))   # Mar 17
    datetime.date(2022, 3, 18)                 # Mar 18

    >>> next_day(dt.date(2022, 3, 31))  # Mar 31
    datetime.date(2022, 4, 1)                 # Apr  1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date + dt.timedelta(days=1)




users = [
  {
    'id': 1,
    'name': 'Employee #1',
    'activated_on': dt.date(2019, 1, 1),
    'deactivated_on': None,
    'customer_id': 1,
  },
  {
    'id': 2,
    'name': 'Employee #2',
    'activated_on': dt.date(2019, 1, 31),
    'deactivated_on': None,
    'customer_id': 1,
  },
]

plan = {
  'id': 1,
  'customer_id': 1,
  'monthly_price_in_cents': 5_000
}

print(monthly_charge('2020-12', plan, users))




































