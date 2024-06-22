#.format method. {} are placeholders and f is saying it's a float and .2 specifies
# the second set following "price"
# Example 1
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# Example 2
'Sam has {0} red balls and {1} yellow balls'.format(12, 31)
# Notes:
# d	for integers
# f	for floating point numbers
# b	for binary numbers
# o	for octal numbers
# x	for octal hexadecimal numbers
# s	for string
# e	for floating point in exponent format
print("Floating point {0:.3f}".format(345.7916732))