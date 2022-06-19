class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        list_suggested_products=[]
        search_word = ''
        for e in searchWord:
            search_word += e
            list_suggested_products.append(self.search(products, search_word))
        return list_suggested_products
            
    def search(self, products, word):
        index=0
        for i, w in enumerate(products):
            if word == w[:len(word)]:
                index=i
                break
        similar_elements = []
        for i in range(index, min(index+3, len(products))):
            if word == products[i][:len(word)]:
                similar_elements.append(products[i])
        return similar_elements