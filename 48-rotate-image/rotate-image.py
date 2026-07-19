class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for layer in range(n//2):
            first = layer
            last = n-1-layer
            for i in range(first, last):
                top = matrix[layer][i]
                matrix[layer][i] = matrix[-i-1][layer]
                matrix[-i-1][layer] = matrix[-layer-1][-i-1]
                matrix[-layer-1][-i-1] = matrix[i][-layer-1]
                matrix[i][-layer-1] = top

            
        