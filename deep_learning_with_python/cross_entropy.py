import math
def cross_entropy(true_dist, predicted_dist):
    '''
     H(p, q) = - p(x) * log(q(x))
    '''
    total_entropy = 0  # This will hold the accumulated value of the cross-entropy calculation
    for true, predicted in zip(true_dist, predicted_dist):
        if predicted == 0:
            continue
        total_entropy -= true * math.log(predicted)
    return total_entropy

true_dist = [1, 0]
predicted_dist = [0.3, 0.7]
entropy_value = cross_entropy(true_dist, predicted_dist)
print(f"Cross entropy: {entropy_value}")
