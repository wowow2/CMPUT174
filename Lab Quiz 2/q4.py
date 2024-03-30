def cdn_tax(income):
    # just a buncha ifs and elifs
    tax = 0
    if income > 246752:
        tax = 55867 * 0.15 + (111733-55867) * 0.205 + (173205-111733) * 0.26 + (246752-173205) * 0.29 + (income - 246752) * 0.33
    elif income > 173205 and income <= 246752:
        tax = 55867 * 0.15 + (111733 - 55867) * 0.205 + (173205 - 111733) * 0.26 + (income - 173205) * 0.29
    elif income > 111733 and income <= 173205:
        tax = 55867 * 0.15 + (111733 - 55867) * 0.205 + (income - 111733) * 0.26
    elif income > 55867 and income <= 111733:
        tax = 55867 * 0.15 + (income - 55867) * 0.205
    elif income <= 55867:
        tax = income * 0.15

    return tax

# Do not touch
def main():
  print(f"{cdn_tax(float(input())):.2f}")

main()