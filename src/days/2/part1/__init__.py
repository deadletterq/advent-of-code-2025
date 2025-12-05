from typing import List, Tuple

def solution(ids: List[Tuple[int, int]]) -> int:
  s = set()
  for (start, end) in ids:
    for i in range(start, end+1):
      v = str(i)
      i_half_1, i_half_2 = v[:len(v)//2], v[len(v)//2:]
      if i_half_1 == i_half_2 and i not in s:
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

