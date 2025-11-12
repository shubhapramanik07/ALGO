# LeetCode 54: Print the Matrix in Spiral Order - Part 43

# there is only one optimal solution....


from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    # """..............................
    #? Return all elements of the matrix in spiral order.
    #? Time complexity: O(m*n)  # overall we visit each of the m*n elements exactly once
    #? Space complexity: O(1) extra, O(m*n) output  # result list holds all elements (output space)
    # """..............................

    # handle empty input (O(1) time, O(1) space)
    if not matrix or not matrix[0]:
        return []

    result: List[int] = []  # output list grows to O(m*n) space as we append elements

    # boundaries for the current layer of the spiral (O(1) time/space)
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    # continue until boundaries cross
    while top <= bottom and left <= right:
        # 1) Traverse from left to right along the top row
        for col in range(left, right + 1):  # visits elements -> contributes to total O(m*n) time
            result.append(matrix[top][col])  # append is amortized O(1); output grows to O(m*n)
        top += 1  # O(1)

        # 2) Traverse from top to bottom along the right column
        for row in range(top, bottom + 1):  # visits elements -> contributes to total O(m*n) time
            result.append(matrix[row][right])  # append amortized O(1)
        right -= 1  # O(1)

        # 3) Traverse from right to left along the bottom row (if still within vertical bounds)
        if top <= bottom:
            for col in range(right, left - 1, -1):  # visits elements -> contributes to total O(m*n) time
                result.append(matrix[bottom][col])  # append amortized O(1)
            bottom -= 1  # O(1)

        # 4) Traverse from bottom to top along the left column (if still within horizontal bounds)
        if left <= right:
            for row in range(bottom, top - 1, -1):  # visits elements -> contributes to total O(m*n) time
                result.append(matrix[row][left])  # append amortized O(1)
            left += 1  # O(1)

    return result

# Example usage / quick tests
if __name__ == "__main__":
    examples = [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
        [[1]],
        [],
        [[1],[2],[3],[4]]
    ]
    for mat in examples:
        print(f"matrix={mat} -> spiral={spiralOrder(mat)}")


# time complexity: O(m*n) coz we visit each element once where m and n are dimensions of matrix 

# space complexity: O(1) extra space (output list is O(m*n) but not counted as extra)