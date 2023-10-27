def avg_calc(*ags):
    if not ags:
        return 0
    total = sum(ags)
    avg = total / len(ags)
    return avg

if __name__ == "__main__":
    a = input("type numbers: ")
    numbers = [float(num) for num in a.split()]
    result = avg_calc(*numbers)
    print(f"Avg: {result}")