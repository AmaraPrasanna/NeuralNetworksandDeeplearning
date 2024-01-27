#Student ID: 700757140
#       CRN :23476

import numpy as np


random_vector = np.random.uniform(1, 20, 20)


reshaped_array = random_vector.reshape(4, 5)


reshaped_array[np.arange(4), np.argmax(reshaped_array, axis=1)] = 0

print("Original random vector:")
print(random_vector)
print("\nReshaped array:")
print(reshaped_array)