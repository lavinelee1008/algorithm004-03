class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five_count = 0
        ten_count = 0
        for money in bills:
            if money == 5:
                five_count += 1
            elif money == 10:
                if five_count >= 1:
                    ten_count += 1
                    five_count -= 1
                else:
                    return False
            else:
                if ten_count >= 1 and five_count >=1:
                    ten_count -= 1
                    five_count -= 1
                elif ten_count == 0 and five_count >= 3:
                    five_count -= 3
                else:
                    return False
        return True