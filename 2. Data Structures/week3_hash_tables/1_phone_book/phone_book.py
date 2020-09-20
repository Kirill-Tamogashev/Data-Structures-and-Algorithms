class Query:

    def __init__(self):
        self.book = [None] * 10000000


    def add(self, number, name):
        self.book[number] = name


    def delete(self, number):
        if self.book[number] is not None:
            self.book[number] = None
    

    def find(self, number):
        if self.book[number] is None:
            return 'not found'
        return self.book[number]


def process_queries(queries):
    for query in queries:
        query = query.split()
        number = int(query[1])
        typ = query[0]

        if typ == 'add':
            q.add(number, query[2])
        elif typ == 'del':
            q.delete(number)
        elif typ == 'find':
            print(q.find(number))



if __name__ == '__main__':
    q = Query()

    n = int(input())
    requests = [input() for _ in range(n)]
    process_queries(requests)

