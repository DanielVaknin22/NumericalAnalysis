import numpy as np

class Spline:
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys
        self.ks = self.get_natural_ks(np.zeros(len(self.xs)))

    def get_natural_ks(self, ks):
        n = len(self.xs) - 1
        A = self._zeros_mat(n + 1, n + 2)

        for i in range(1, n):
            A[i][i - 1] = 1 / (self.xs[i] - self.xs[i - 1])
            A[i][i] = 2 * (1 / (self.xs[i] - self.xs[i - 1]) + 1 / (self.xs[i + 1] - self.xs[i]))
            A[i][i + 1] = 1 / (self.xs[i + 1] - self.xs[i])
            A[i][n + 1] = 3 * (
                ((self.ys[i] - self.ys[i - 1]) / ((self.xs[i] - self.xs[i - 1]) * (self.xs[i] - self.xs[i - 1]))) +
                ((self.ys[i + 1] - self.ys[i]) / ((self.xs[i + 1] - self.xs[i]) * (self.xs[i + 1] - self.xs[i])))
            )

        A[0][0] = 2 / (self.xs[1] - self.xs[0])
        A[0][1] = 1 / (self.xs[1] - self.xs[0])
        A[0][n + 1] = (3 * (self.ys[1] - self.ys[0])) / ((self.xs[1] - self.xs[0]) * (self.xs[1] - self.xs[0]))

        A[n][n - 1] = 1 / (self.xs[n] - self.xs[n - 1])
        A[n][n] = 2 / (self.xs[n] - self.xs[n - 1])
        A[n][n + 1] = (3 * (self.ys[n] - self.ys[n - 1])) / ((self.xs[n] - self.xs[n - 1]) * (self.xs[n] - self.xs[n - 1]))

        return self._solve(A, ks)

    def _index_before(self, target):
        low = 0
        high = len(self.xs)
        mid = 0
        while low < high:
            mid = (low + high) // 2
            if self.xs[mid] < target and mid != low:
                low = mid
            elif self.xs[mid] >= target and mid != high:
                high = mid
            else:
                high = low

        if low == len(self.xs) - 1:
            return len(self.xs) - 1
        return low + 1

    def _solve(self, A, ks):
        m = len(A)
        h = 0
        k = 0
        while h < m and k <= m:
            i_max = max(range(h, m), key=lambda i: abs(A[i][k]))
            if A[i_max][k] == 0:
                k += 1
            else:
                A[h], A[i_max] = A[i_max], A[h]
                for i in range(h + 1, m):
                    f = A[i][k] / A[h][k]
                    A[i][k] = 0
                    for j in range(k + 1, m + 1):
                        A[i][j] -= A[h][j] * f
                h += 1
                k += 1

        for i in range(m - 1, -1, -1):
            v = 0
            if A[i][i]:
                v = A[i][m] / A[i][i]
            ks[i] = v
            for j in range(i - 1, -1, -1):
                A[j][m] -= A[j][i] * v
                A[j][i] = 0
        return ks

    def _zeros_mat(self, r, c):
        return np.zeros((r, c))

    def at(self, x):
        i = self._index_before(x)
        t = (x - self.xs[i - 1]) / (self.xs[i] - self.xs[i - 1])
        a = self.ks[i - 1] * (self.xs[i] - self.xs[i - 1]) - (self.ys[i] - self.ys[i - 1])
        b = -self.ks[i] * (self.xs[i] - self.xs[i - 1]) + (self.ys[i] - self.ys[i - 1])
        q = (1 - t) * self.ys[i - 1] + t * self.ys[i] + t * (1 - t) * (a * (1 - t) + b * t)
        return q

if __name__ == "__main__":
        # Given points
        points = [(0.35, -3.65), (0.4, -3), (0.55, -2.6), (0.65, 0.2), (0.7, 1.67)]

        # Separate x and y coordinates
        xs = [point[0] for point in points]
        ys = [point[1] for point in points]

        # Create a spline
        spline = Spline(xs, ys)

        x_values = [0.45, 0.6]
        for x_val in x_values:
            interpolated_value = spline.at(x_val)
            print(f"f({x_val}) = {interpolated_value}")