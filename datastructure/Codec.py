import random


class Codec:
    def __init__(self):
        self.map = {}
        self.string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = self.getrand()

    def getrand(self):
        res = ""
        for i in range(6):
            idx = random.randint(0, 62)
            res += self.string[idx]
        return res

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while self.key in self.map:
            self.key = self.getrand()
        self.map[self.key] = longUrl
        return "http://tinyurl.com/" + self.key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map[shortUrl.replace("http://tinyurl.com/", "")]
