# expression = input()
expression = '{([]){}()}'
# expression = ']['
brackets = [('(', ')'),
            ('[', ']'),
            ('{', '}')]

counts = all([expression.count(a) == expression.count(b) for a, b in brackets])     # do all bracket pairs counts match?
order = all([expression.find(a) <= expression.find(b) for a, b in brackets])        # is the order right?
print("true" if order and counts else "false")
