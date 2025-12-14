class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        valid_lines = {"electronics", "grocery", "pharmacy", "restaurant"}
        valid_coupons = []

        for c, b, active in zip(code, businessLine, isActive):
            if not c:
                continue

            # validate characters
            for ch in c:
                if not ch.isalnum() and ch != "_":
                    break
            else:
                # runs only if loop didn't break
                if b in valid_lines and active:
                    valid_coupons.append((b, c))

        valid_coupons.sort()  # sorts by businessLine, then code
        return [c for _, c in valid_coupons]
            