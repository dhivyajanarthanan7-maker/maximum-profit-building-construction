
buildings = {
    "T": (5, 1500),   # Theatre: construction time, earning rate
    "P": (4, 1000),   # Pub
    "C": (10, 2000)   # Commercial Park
}


def max_profit(total_time):
    max_earnings = 0
    best_plans = []

    def calculate(time_used, earnings, t, p, c):
        nonlocal max_earnings, best_plans

        if earnings > max_earnings:
            max_earnings = earnings
            best_plans = [(t, p, c)]
        elif earnings == max_earnings:
            if (t, p, c) not in best_plans:
                best_plans.append((t, p, c))

        for name, (build_time, rate) in buildings.items():
            finish_time = time_used + build_time

            if finish_time <= total_time:
                operating_time = total_time - finish_time
                building_earnings = operating_time * rate

                if name == "T":
                    calculate(finish_time, earnings + building_earnings,
                              t + 1, p, c)
                elif name == "P":
                    calculate(finish_time, earnings + building_earnings,
                              t, p + 1, c)
                else:
                    calculate(finish_time, earnings + building_earnings,
                              t, p, c + 1)

    calculate(0, 0, 0, 0, 0)

    return max_earnings, best_plans


# Test the program
times = [11]

for n in times:
    earnings, plans = max_profit(n)

    print(f"\nTotal time: {n}")
    print(f"Maximum earnings: ${earnings:,}")

    for t, p, c in plans:
        print(f"Theatre: {t}, Pub: {p}, Commercial Park: {c}")
