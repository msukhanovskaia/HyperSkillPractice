squares = {1: 1, 3: 9, 5: 25, 6: 36, 8: 64, 10: 100, 11: 121, 15: 225}
input_key = int(input())
print("There is no such key" if input_key not in squares else squares.get(input_key))
if input_key in squares: del squares[input_key]
print(squares)
