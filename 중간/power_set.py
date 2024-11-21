# rets = []

# def _power_set(A, idx, used):
#     if idx == len(A):
#         ret = []
#         for i in range(len(A)):
#             if used[i]:
#                 ret.append(A[i])
#         rets.append(ret)
#         return
#     used[idx] = True
#     _power_set(A, idx + 1, used)
#     used[idx] = False
#     _power_set(A, idx + 1, used)


# def power_set(A: list[int]) -> list[list[int]]:
#     used = [False] * len(A)
#     _power_set(A, 0, used)
#     return rets

def _power_set(A: list[int], idx: int, used: list[bool], ret: list[list[int]]):
    if idx == len(A):
        res = []
        for i in range(len(used)):
            if used[i]:
                res.append(A[i])
        ret.append(res)
        return
    used[idx] = True
    _power_set(A, idx + 1, used, ret)
    used[idx] = False
    _power_set(A, idx + 1, used, ret)

def power_set(A: list[int]) -> list[list[int]]:
    used = [False] * len(A)
    ret = []
    _power_set(A, 0, used, ret)
    return ret

if __name__ == "__main__":
    lst = [1, 2, 3]
    out = power_set(lst)
    print(out)