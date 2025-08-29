import random

kata_list = ["python", "robot", "komputer", "internet", "arduino"]
kata = random.choice(kata_list)
tebakan = ["_"] * len(kata)

print("=== Game Tebak Kata ===")
print(" ".join(tebakan))

kesempatan = 6
while kesempatan > 0 and "_" in tebakan:
    huruf = input("Tebak huruf: ").lower()
    if huruf in kata:
        for i, h in enumerate(kata):
            if h == huruf:
                tebakan[i] = huruf
    else:
        kesempatan -= 1
        print("Salah! Kesempatan tersisa:", kesempatan)

    print(" ".join(tebakan))

if "_" not in tebakan:
    print("Selamat! Kata:", kata)
else:
    print("Game Over! Kata yang benar:", kata)
