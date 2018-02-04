import math


class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        init = list(board[0]) + list(board[1])
        possible = []

        def move(poss, state, step):
            if state == [1, 2, 3, 4, 5, 0]:
                print(step)
                return step
            elif state in poss:
                print("asd")
                return math.inf
            else:
                poss.append(state)
                if state[0] == 0:
                    t1 = [state[1], state[0], state[2], state[3], state[4], state[5]]
                    t2 = [state[3], state[1], state[2], state[0], state[4], state[5]]
                    return min(move(poss[:], t1, step + 1), move(poss[:], t2, step + 1))
                elif state[1] == 0:
                    t1 = [state[1], state[0], state[2], state[3], state[4], state[5]]
                    t2 = [state[0], state[2], state[1], state[3], state[4], state[5]]
                    t3 = [state[0], state[4], state[2], state[3], state[1], state[5]]
                    return min(move(poss[:], t1, step + 1), min(move(poss[:], t2, step + 1), move(poss[:], t3, step + 1)))
                elif state[2] == 0:
                    t1 = [state[0], state[2], state[1], state[3], state[4], state[5]]
                    t2 = [state[0], state[1], state[5], state[3], state[4], state[2]]
                    return min(move(poss[:], t1, step + 1), move(poss[:], t2, step + 1))
                elif state[3] == 0:
                    t1 = [state[3], state[1], state[2], state[0], state[4], state[5]]
                    t2 = [state[0], state[1], state[2], state[4], state[3], state[5]]
                    return min(move(poss[:], t1, step + 1), move(poss[:], t2, step + 1))
                elif state[4] == 0:
                    t1 = [state[0], state[1], state[2], state[3], state[5], state[4]]
                    t2 = [state[0], state[4], state[2], state[3], state[1], state[5]]
                    t3 = [state[0], state[1], state[2], state[4], state[3], state[5]]
                    return min(move(poss[:], t1, step + 1), min(move(poss[:], t2, step + 1), move(poss[:], t3, step + 1)))
                elif state[5] == 0:
                    t1 = [state[0], state[1], state[5], state[3], state[4], state[2]]
                    t2 = [state[0], state[1], state[2], state[3], state[5], state[4]]
                    return min(move(poss[:], t1, step + 1), move(poss[:], t2, step + 1))

        return move(possible, init, 0)


if __name__ == '__main__':
    s = Solution()
    print(s.slidingPuzzle(board=[[4, 1, 2], [5, 0, 3]]))
