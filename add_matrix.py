def matrix_add(A_str, B_str):
    A = parse_matrix(A_str)
    B = parse_matrix(B_str)

    validate_same_dimension(A, B)

    result = [
        [A[i][j] + B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]

    return str(result)
