class BigInteger:
    def plus_one(self, digits: list[int]) -> list[int]:
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

    def plus_one_48ms(self, digits: list[int]) -> list[int]:
        length = len(digits)
        sum = 0
        for i in range(length):
            sum += digits[i] * pow(10,length-i-1)
        sum += 1
        return [int(x) for x in str(sum)]

    def plus_one_fastest(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1]+digits
