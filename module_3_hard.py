from string import capwords


def calculate_structure_sum(*args):
  structure = args
  summa = 0
  for i in structure:
    if isinstance(i, str):
      summa += len(i)
    elif isinstance(i, (float, int)):
      summa += i
    elif isinstance(i, dict):
      i = list(i.items())
      summa += calculate_structure_sum(*i)
    elif isinstance(i, bool):
      summa += int(i)
    else:
      summa += calculate_structure_sum(*i)
  return summa


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)