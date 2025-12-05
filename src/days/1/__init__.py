from typing import List


def solution(rotations: List[str]) -> int:
  pos = 50
  count = 0
  for rotation in rotations:
    direction, amount = rotation[0], int(rotation[1:])
    if direction == 'L': pos = (pos - amount) % 100
    elif direction == 'R': pos = (pos + amount) % 100

    if pos == 0: count += 1
  return count

def main():
  file = "input.txt"
  with open(file) as f:
    input = f.read().splitlines()
    result = solution(input)
    print("Result:", result)

if __name__ == "__main__":
  main()

