""" 
자료 구조 - 해시 테이블
"""

# 해시 테이블 구현

class Hash_Table:
    def __init__(self, length = 5):
        self.max_len = length
        self.table = [[] for _ in range(self.max_len)]

    def hash(self, key):
        res = sum([ord(s) for s in key])
        return res % self.max_len
    
    def set(self, key, value):
        index = self.hash(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        value = self.table[index]
        if not value:
            return None
        
        for v in value:
            if v[0] == key:
                return v[1]
        return None
    

if __name__ == "__main__":
    capital = Hash_Table()
    country = ["Korea", "America", "China", "England", "Türkiye"]
    city = ["Seoul", "Washington", "Beijing", "London", "Ankara"]

    for co, ci in zip(country, city):
        capital.set(co, ci)

    print("해시 테이블의 상태")
    print("===============")
    for i, v in enumerate(capital.table):
        print(i, v)
    print()
    print("해시 테이블의 검색 결과")
    print("====================")
    print(f"Captial of America = {capital.get('America')}")
    print(f"Captial of Korea = {capital.get('Korea')}")
    print(f"Captial of England = {capital.get('England')}")
    print(f"Captial of China = {capital.get('China')}")
    print(f"Captial of Japan = {capital.get('Japan')}")
    print(f"Captial of Türkiye = {capital.get('Türkiye')}")


    # 파이썬의 딕셔너리 자료구조를 해시 테이블로 활용할 수 있다.