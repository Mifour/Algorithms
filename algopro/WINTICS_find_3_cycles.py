"""
Does a graph has a 3 cycle, yes or no?
O(n^2) time & space
"""
def has_3c(graph):
  nodes = [] 
  adja = {}
  for x,y in graph:
    adja[x] = adja[x] + [y] if x in adja else [y]
    adja[y] = adja[y] + [x] if y in adja else [x]
    
  for node in adja:
    if len(adja[node]) > 1:
      for linked in adja[node]:
        if set(adja[node]).intersection(set(adja[linked])):
          return True
  return False


graph = [(0, 1), (0, 2), (1, 2), (1, 3), (3, 4), (2, 4)]
print(has_3c(graph))
