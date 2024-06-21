class HexVal:
  def __init__(self, value, isChar = False):
    if isChar:
      decValue = ord(value)
      self.value = hex(decValue)
    else:
      self.value = value
        

  def __str__(self):
    return f"{self.value}"
  
  def add(self, other):
    return hex(int(self.value, 16) + int(other.value, 16))
  
  def sub(self, other):
    return hex(int(self.value, 16) - int(other.value, 16))
  
# hex1 = HexVal(' ', True)
# hex2 = HexVal('C', True)


# print(hex1)
# print(hex2)
# print(hex1.add(hex2))
# print(hex1.sub(hex2))
