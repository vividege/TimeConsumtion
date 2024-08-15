class BigInteger:
    def plus_one_48ms(self, digits: list[int]) -> list[int]:
        add_flag = 1
        for i in range(len(digits) - 1, -1, -1):
            if add_flag == 0:
                break
            temp = digits[i] + add_flag
            if temp >= 10:
                temp = temp - 10
                add_flag = 1
            else:
                add_flag = 0
            digits[i] = temp
        if add_flag == 1:
            ret = [1]
            ret.extend(digits)
        else:
            ret = digits
        return ret


if __name__ == '__main__':
    b = BigInteger()
    b.plus_one_48ms([9])
