def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    matrix = []
    
    with open(csv_file_path) as csvDataFile:
        csvRows = csvDataFile.readlines()

        for row in csvRows:
            data = row.strip().split(",")
            matrix.append([eval(val) for val in data])
            
    return matrix
