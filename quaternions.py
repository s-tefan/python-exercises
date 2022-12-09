class Quaternion:
    def __init__(self, re=0, im=(0, 0, 0)):
        self.real = re
        self.imag = im

    def conj(self):
        return Quaternion(self.real, tuple(-k for k in self.imag))

    def __add__(self, a):
        if isinstance(a, Quaternion):
            return Quaternion(
                self.real + a.real, tuple(self.imag[k] + a.imag[k] for k in range(3))
            )
        else:
            return Quaternion(self.real + a.real, self.imag)

    def __neg__(self):
        return Quaternion(-self.real, tuple(-k for k in self.imag))

    def __sub__(self, a):
        return self + (-a)

    def __mul__(self, a):
        if isinstance(a, Quaternion):
            u = self.imag
            v = a.imag
            re = self.real * a.real - sum(u[k] * v[k] for k in range(3))
            imlist = [0, 0, 0]
            for k in range(3):
                imlist[k] = (
                    self.real * v[k]
                    + a.real * u[k]
                    + u[(k + 1) % 3] * v[(k - 1) % 3]
                    - v[(k + 1) % 3] * u[(k - 1) % 3]
                )
            return Quaternion(re, tuple(imlist))
        else:
            return Quaternion(self.real * a, self.imag)

    def __str__(self):
        return "({} + {}i + {}j + {}k)".format(
            self.real, self.imag[0], self.imag[1], self.imag[2]
        )

    def __repr__(self):
        return (self.real, self.imag)


if __name__ == "__main__":
    import math

    def test():
        i = Quaternion(0, (1, 0, 0))
        j = Quaternion(0, (0, 1, 0))
        print(
            "i = {}, j = {}, i*i = {}, i*j = {}, j*i = {}".format(
                i, j, i * i, i * j, j * i
            )
        )

        v = (1 / 3 ** (1 / 2),) * 3
        th = math.pi / 6
        vs = tuple(k * math.sin(th) for k in v)
        s = Quaternion(math.cos(th), vs)
        print(s)
        b = i
        for k in range(13):
            print(b)
            b = s * b * s.conj()
