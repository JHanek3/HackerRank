# Task
# Given a string S
# Task is to find the indices of the start and end of string k in S

import re
# S = "aaadaa"
# k ="aa"


S, k = input(), input()
matches = list(re.finditer(r'(?={})'.format(k), S))
if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(k) - 1)) for match in matches))
else:
    print('(-1, -1)')