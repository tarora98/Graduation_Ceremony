class GraduationCeremony:

    def __init__(self, n, m):
        # n: number of academic days
        # m: cannot miss m the class for four or more consecutive days

        if n < m or n < 0 or m < 0:
            raise Exception("Invalid Inputs")

        self.n = n
        self.m = m

    def process(self):
        """
        Time Complexity: O(m * n)
        Space Complexity: O(m)
        """

        n, m = self.n, self.m
        dp = [1] * (m + 1)
        dp[m] = 0

        for i in range(1, n + 1):
            temp = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                temp[j] = dp[0] + dp[j + 1]

            temp, dp = dp, temp

        c1 = dp[0]  # total number of valid way to attend classes
        c2 = temp[1]  # total number of way to miss last day

        return f"{c2}/{c1}"

    def display(self):
        result = self.process()
        print(result)

if __name__ == "__main__":

    inputs = [(5, 4), (10, 4)]
    
    for n, m in inputs:
        obj = GraduationCeremony(n, m)
        obj.display()
