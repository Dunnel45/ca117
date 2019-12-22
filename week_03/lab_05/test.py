import sys

def top_time(lines):
    top = 1000
    best_time = None
    best_name = None
    invalid = []
    for l in lines:
        details = l.split(" ")
        name = details[0]
        times = details[1:]
        try:
            for t in times:
                mins, sec = t.split(":")
                conv = (int(mins) * 60) + int(sec)
                if conv < int(top):
                    best_time = t
                    top = conv
                    best_name = name
        except ValueError:
            invalid.append(name)

    print("{} is the fastest runner with a time of {}".format(best_name, best_time))
    for runner in invalid:
        print("{} was disqualified for an invalid time".format(runner))

def main():
        lines = [l for l in sys.stdin]
        (top_time(lines))

if __name__ == "__main__":
    main()
