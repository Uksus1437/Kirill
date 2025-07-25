# ((x ∧ y) ∨ (y ∧ z)) ≡ ((x → w) ∧ (w → z))        -> 1

# ∧ - and
# ∨ - or
# → - <=
# ≡ - ==
# ¬ - not

print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (w <= y) and (not(y) == x) and (x or z):
                    print(x, y, z, w)