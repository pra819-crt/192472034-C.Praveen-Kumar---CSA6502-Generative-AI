from sklearn.metrics.pairwise import cosine_similarity

vector1 = [[1, 2, 3]]
vector2 = [[2, 4, 6]]

result = cosine_similarity(vector1, vector2)

print("Cosine Similarity:")
print(result)
