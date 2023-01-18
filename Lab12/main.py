import json


class Solution:
    def sum_number_in_string(self, number_string: str) -> int:
        S = 0
        for i in range(len(number_string)):
            num = int(number_string[i])
            S += num
        print(S)

    def get_leader_string(self, steps: int) -> str:
        result = ""
        for i in range(steps + 1):
            str = ""
            for j in range(steps - i):
                str += ' '
            for j in range(i):
                str += '#'
            result += str + '\n'
        return result

    def to_json(self, func):
        def wrapped(*args, **kwargs):
            return json.dumps(func(*args, **kwargs))
        return wrapped

    def get_spiral_number_matrix(self, number: int) -> str:
        rowStart = 0
        colStart = 0
        rowEnd = number
        colEnd = number
        result = [[0 for i in range(number)] for j in range(number)]
        temp = 1
        while temp <= number**2:
            for i in range(colStart, colEnd):
                result[rowStart][i] = temp
                temp += 1
            if temp > number**2:
                break
            for i in range(rowStart+1, rowEnd):
                result[i][colEnd-1] = temp
                temp += 1
            if temp > number**2:
                break
            for i in range(colEnd-2, colStart-1, -1):
                result[rowEnd-1][i] = temp
                temp += 1
            if temp > number**2:
                break
            for i in range(rowEnd-2, rowStart, -1):
                result[i][colStart] = temp
                temp += 1
                rowStart += 1
                rowEnd -= 1
                colStart += 1
                colEnd -= 1
                # print(result)
        return result


def main():
    solution = Solution()
    solution.sum_number_in_string('12345')
    solution.sum_number_in_string('160438521039')
    print(solution.get_leader_string(3))
    print(solution.get_leader_string(5))

    @solution.to_json
    def get_data():
        return {
            'data': 42
        }

    print(get_data())


if __name__ == '__main__':
    main()
