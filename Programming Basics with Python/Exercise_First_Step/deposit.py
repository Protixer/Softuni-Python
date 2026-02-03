deposit = float(input())
finish_time = int(input())
procent = float(input())

lihva = deposit * (procent / 100)
mesechna_lihva = lihva / 12
print(f"{deposit + (finish_time * mesechna_lihva)}")