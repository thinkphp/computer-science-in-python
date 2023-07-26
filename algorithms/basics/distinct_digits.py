def fn():
    def check_distinct(nr):
        n2 = 0
        while nr > 9 and n2 == 0:
            last = nr % 10
            n2 = nr // 10

            while n2!=0 and n2%10 != last:
                n2//=10
            nr//=10
        return n2

    nr = 123447
    ans = check_distinct(nr)
    if ans == 0:
        print("Distinct Digits.");
    else:
        print("Not Distinct Digits.")
fn()
