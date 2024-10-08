def isSubsequence(s: str, t: str) -> bool:
    pointer_s = 0
    pointer_t = 0
    
    while pointer_s < len(s) and pointer_t < len(t):
        if s[pointer_s] == t[pointer_t]:
            pointer_s += 1
        pointer_t += 1

    return pointer_s == len(s)

# Ví dụ kiểm tra
# print(isSubsequence("ace", "abcde"))  # Output: True
# print(isSubsequence("axc", "ahbgdc"))  # Output: False
while True:
    s = input("Nhập s: ")
    t = input("Nhập t: ")
    if len(s) > 100 or len(t) > 10**4:
        print("Quá dài")
        pass
    else:
        print(isSubsequence(s, t))