def isValid(n:int, x:int, y:int) -> bool:
    return not rowUsed[x] and not colUsed[y] and not diagUsed1[x + y] and not diagUsed2[x - y + n]

def setUsed(n: int, x:int, y:int, state: bool):
    rowUsed[x] = state
    colUsed[y] = state
    diagUsed1[x + y] = state
    diagUsed2[x - y + n] = state

def _n_queen(n:int, row: int):
    if row == n:
        return 1
    ret = 0
    for col in range(n):
        if isValid(n, row, col):
            setUsed(n, row, col, True)
            ret += _n_queen(n, row + 1)
            setUsed(n, row, col, False)
    return ret

def n_queen(n: int) -> int:
    return _n_queen(n, 0)

if __name__ == "__main__":
    for n in range(15):
        rowUsed = [0] * n
        colUsed = [0] * n
        diagUsed1 = [0] * 2 * n
        diagUsed2 = [0] * 2 * n
        # print(n, n_queen(n))
        flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]