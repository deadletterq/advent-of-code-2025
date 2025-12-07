from typing import List

def solution(rows: List[List[int]]) -> int:
  sum = 0
  for i in range(len(rows)):
    biggest_number_so_far = rows[i][0]
    biggest_candidate = 0
    for j in range(1, len(rows[i])):
      biggest_candidate = max(biggest_candidate, int(f"{biggest_number_so_far}{rows[i][j]}"))
      biggest_number_so_far = max(biggest_number_so_far, rows[i][j])
    sum += biggest_candidate
  return sum

def main():
  file = "input.txt"
  with open(file) as f:
    input = f.read().splitlines()
    mapped = list(map(lambda x: list(map(int, x)), input))
    result = solution(mapped)
    print("Result:", result)

if __name__ == "__main__":
  main()

