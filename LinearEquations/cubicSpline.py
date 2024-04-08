import numpy as np

class CubicSpline:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.a, self.b, self.c, self.d = self.compute_cubic_spline()

    def compute_cubic_spline(self):
        h = np.diff(self.x)
        delta = np.diff(self.y)
        alpha = np.zeros(self.n)
        for i in range(1, self.n - 1):
            alpha[i] = 3 / h[i] * (delta[i] / h[i] - delta[i - 1] / h[i - 1])
        l, mu, z = np.zeros(self.n), np.zeros(self.n), np.zeros(self.n)
        l[0] = 1
        mu[0] = z[0] = 0
        c = np.zeros(self.n)  # Initialize c array here
        for i in range(1, self.n - 1):
            l[i] = 2 * (self.x[i + 1] - self.x[i - 1]) - h[i - 1] * mu[i - 1]
            mu[i] = h[i] / l[i]
            z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]
        l[-1] = 1
        z[-1] = c[-1] = 0
        a, b, d = np.zeros(self.n), np.zeros(self.n), np.zeros(self.n)  # Remove c from here
        for j in range(self.n - 2, -1, -1):
            c[j] = z[j] - mu[j] * c[j + 1]
            b[j] = delta[j] / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
            d[j] = (c[j + 1] - c[j]) / (3 * h[j])
            a[j] = self.y[j]
        return a, b, c, d

    def interpolate(self, x_val):
        i = np.searchsorted(self.x, x_val) - 1
        if i == self.n - 1:
            i -= 1
        dx = x_val - self.x[i]
        return self.a[i] + self.b[i] * dx + self.c[i] * dx ** 2 + self.d[i] * dx ** 3

if __name__ == '__main__':
    x = np.array([-1, 0, 1])
    y = np.array([1, 0, 1])

    cubic_spline = CubicSpline(x, y)
    cubic_spline.c[0] = -3  # f'(-1) = -3
    cubic_spline.c[-1] = 3  # f'(1) = 3

    natural_spline = CubicSpline(x, y)
    natural_spline.c[0] = natural_spline.c[-1] = 0

    x_val = 0.5
    interpolated_value_cubic = cubic_spline.interpolate(x_val)
    interpolated_value_natural = natural_spline.interpolate(x_val)
    print(f"Interpolated value at x={x_val} (Cubic Spline): {interpolated_value_cubic}")
    print(f"Interpolated value at x={x_val} (Natural Spline): {interpolated_value_natural}")
