from problems.dp.edit_distance import edit_distance

def main():
    out = edit_distance("POLYNOMIAL", "EXPONENTIAL")
    print(out)

if __name__ == '__main__':
    main()