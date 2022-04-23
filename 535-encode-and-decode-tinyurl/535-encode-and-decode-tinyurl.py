class Codec:
    def __init__(self):
        self.lookup = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        n = len(self.lookup)
        self.lookup.append(longUrl)
        return "http://tinyurl.com/" + str(n)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        s = int(shortUrl.split('/')[-1])
        return self.lookup[s]