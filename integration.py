import numpy as np
import tensornetics

# Set up the integration matrices
matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])

# Integrate the matrices using element-wise multiplication
integrated_matrix = matrix_1 * matrix_2
print(integrated_matrix)  # [[5, 12], [21, 32]]

# Set up the vectorized database
database = tensornetics.VectorizedDatabase()

# Add the integrated matrix to the database
database.add_data(integrated_matrix)

# Retrieve the integrated matrix from the database
retrieved_matrix = database.get_data()
print(retrieved_matrix)  # [[5, 12], [21, 32]]
