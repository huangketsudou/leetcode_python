class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dictionary=defaultdict(int)
        for cpdomain in cpdomains:
            num,cp=cpdomain.split(' ')
            num=int(num)
            while True:
                dictionary[cp]+=num
                cut=cp.split('.',1)
                if len(cut)==1:
                    break
                cp=cut[1]
        #return ["{} {}".format(ct, dom) for dom, ct in dictionary.items()]
        return list(map(lambda x,y:str(y)+' '+x,dictionary.keys(),dictionary.values()))


class Solution(object):
    def subdomainVisits(self, cpdomains):
        ans = Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]



k=Solution()
print(k.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
