import math

# 1. 'points' adında bir liste oluşturun
points = [(1, 2), (4, 6), (5, 8), (9, 10)]

# 2. 'euclideanDistance' adında bir fonksiyon tanımlayın
def euclideanDistance(point1, point2):
    return math.sqrt((point2 - point1)**2 + (point2 - point1)**2)

# 3. Mesafeleri hesaplayın ve 'distances' listesinde saklayın
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# 4. 'distances' listesinden minimum mesafeyi bulun ve yazdırın
min_distance = min(distances)
print(f"Minimum Öklid mesafesi: {min_distance}")
