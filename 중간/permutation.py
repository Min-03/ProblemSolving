import sys

# rets = []

# def _permute(s, order, orders):
#     if len(orders) == order:
#         ret = ["0"] * len(s)
#         for i, order in enumerate(orders):
#             ret[order] = s[i]
#         rets.append("".join(ret))
#         return
#     for i in range(len(orders)):
#         if orders[i] == -1:
#             orders[i] = order
#             _permute(s, order + 1, orders)
#             orders[i] = -1

# def permute(s: str) -> list[str]:
#     orders = [-1] * len(s)
#     _permute(s, 0, orders)
#     return rets

def _permute(s: list[str], idx: int, ans: list[str]):
    if idx == len(s):
        ans.append("".join(s))
        return
    for i in range(idx, len(s)):
        s[idx], s[i] = s[i], s[idx]
        _permute(s, idx + 1, ans)
        s[idx], s[i] = s[i], s[idx]

def permute(s: str) -> list[str]:
    rets = []
    _permute(list(s), 0, rets)
    return rets
    
if __name__ == "__main__":
    out = permute(sys.argv[1])
    print(out)