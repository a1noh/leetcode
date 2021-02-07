import collections
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = collections.defaultdict(int)
        for i in cpdomains:
            item = i.split(" ")
            num = item[0]
            domain = item[1].split(".")
            temp = ""
            for i in domain[::-1]:
                if temp == "":
                    temp = i
                else:
                    temp = i + "."+ temp
                d[temp] += int(num)
        # print(d)
        ans = []
        for key in d:
            ans.append(str(d[key]) + " " + key)
        print(ans)
        return ans
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

sol = Solution()
sol.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])