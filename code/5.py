def datafile():
    with open('5_seat.txt', 'r') as d:
        data = d.read()
        data = data.split()
        d.close()
        return data


def seat_row(tickets):
    rows = []
    for ticket in tickets:
        row = 0
        if ticket[0] == "B":
            row = row + 64
        else:
            row = row
        if ticket[1] == "B":
            row = row + 32
        else:
            row = row
        if ticket[2] == "B":
            row = row + 16
        else:
            row = row
        if ticket[3] == "B":
            row = row + 8
        else:
            row = row
        if ticket[4] == "B":
            row = row + 4
        else:
            row = row
        if ticket[5] == "B":
            row = row + 2
        else:
            row = row
        if ticket[6] == "B":
            row = row + 1
        else:
            row = row
        rows.append(row)
    return rows


def seat_column(tickets):
    columns = []
    for ticket in tickets:
        column = 0
        if ticket[7] == "R":
            column = column + 4
        else:
            column = column
        if ticket[8] == "R":
            column = column + 2
        else:
            column = column
        if ticket[9] == "R":
            column = column + 1
        else:
            column = column
        columns.append(column)
    return columns


if __name__ == '__main__':
    ids = []
    for id in range(len(datafile())):
        idn = (seat_row(datafile())[id]*8)+seat_column(datafile())[id]
        ids.append(idn)

    print(max(ids))
