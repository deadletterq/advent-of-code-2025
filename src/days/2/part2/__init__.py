from typing import List, Tuple

def all_parts_equal(parts: List[List[str]]) -> bool:
  for part in parts:
    s = set(part)
    if len(s) == 1:
      return True
  return False

def solution(ids: List[Tuple[int, int]]) -> int:
  s = set()
  for (start, end) in ids:
    for i in range(start, end+1):
      v = str(i)
      double = v + v
      if double.find(v, 1) != len(v):
        s.add(i)

  return sum(s)

def main():
  file = "input.txt"
  with open(file) as f:
    input = f.read().splitlines()[0].split(",")
    mapped = list(map(lambda x: (int(x.split("-")[0]), int(x.split("-")[1])), input))
    result = solution(mapped)
    print("Result:", result)

if __name__ == "__main__":
  main()

