import pandas as pd


def main():
    # File read
    file_in = pd.read_csv('input.csv', encoding="UTF-8")
    time = file_in['Time']
    x = file_in['x']
    print(file_in)

    # File write
    file_out = pd.DataFrame(columns=['Time', 'x'])
    for i in range(len(file_in)):
        tmp = pd.Series([time[i], x[i]], index=file_out.columns)
        file_out = file_out.append(tmp, ignore_index=True)
    file_out.to_csv('output.csv', index=False)


if __name__ == "__main__":
    main()
