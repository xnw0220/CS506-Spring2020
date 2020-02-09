def euclidean_dist(x, y):
    return (sum([(a - b) ** 2 for a, b in zip(x, y)]))**(1/2)

def manhattan_dist(x, y):
    return sum(abs(a-b) for a,b in zip(x,y))

def jaccard_dist(x, y):
    set_x = set(x)
    set_y = set(y)
    size_x = len(set_x)
    size_y = len(set_y)
    intersect = set_x & set_y
    size_intersect = len(intersect)
    jaccard_sim = size_intersect / (size_x + size_y - size_intersect)
    return 1 - jaccard_sim

def cosine_sim(x, y):
    dot_product_xy = sum(map(lambda z: z[0] * z[1], zip(x, y)))
    dot_product_xx = sum(map(lambda z: z[0] * z[1], zip(x, x)))
    dot_product_yy = sum(map(lambda z: z[0] * z[1], zip(y, y)))
    len_x = (dot_product_xx)**(1/2)
    len_y = (dot_product_yy)**(1/2)
    cosine_sim = dot_product_xy / (len_x * len_y)
    return cosine_sim

# Feel free to add more
