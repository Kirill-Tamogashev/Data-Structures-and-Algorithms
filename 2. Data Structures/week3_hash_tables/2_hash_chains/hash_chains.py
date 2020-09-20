class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007


    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elems = [[] for _ in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def add(self, string):
        h = self._hash_func(string)
        if string not in self.elems[h]:
            self.elems[h].append(string)

    def delete(self, string):
        h = self._hash_func(string)
        if string in self.elems[h]:
            self.elems[h].remove(string)
    
    def find(self, string):
        h = self._hash_func(string)
        if string in self.elems[h]:
            print('yes')
        else:
            print('no')
    
    def check(self, number):
        number = int(number)
        print(*self.elems[number][::-1])



def process_query(query):
    comand, arg = query.split()
    if comand == "check":
        proc.check(arg)
        
    elif comand == "add":
        proc.add(arg)
        
    elif comand == "del":
        proc.delete(arg)

    elif comand == "find":
        proc.find(arg)

def process_queries():
    n = int(input())
    queries = [input() for _ in range(n)] 
    for query in queries:
        process_query(query)

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    process_queries()
