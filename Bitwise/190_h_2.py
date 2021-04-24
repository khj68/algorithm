def reverseBits(self, n: int) -> int:
  # print('0'*(32 - len(bin(n)[2:])) + bin(n)[2:])
  # print(int(('0'*(32 - len(bin(n)[2:])) + bin(n)[2:])[::-1], 2))
  return int(('0'*(32 - len(bin(n)[2:])) + bin(n)[2:])[::-1], 2)



print(reverseBits(0, 43261596))