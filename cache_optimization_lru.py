import functools
import cv2
import tensorflow as tf

@functools.lru_cache(maxsize=128)
def classify_image(image, patch_size=None):
    # Load a deep learning model and prepare the input tensor
    model = tf.saved_model.load("model")
    input_data = tf.constant(image, dtype=tf.float32)

    # Split the input image into patches, if patch_size is specified
    if patch_size is not None:
        patches = cv2.split(image)
    else:
        patches = [image]

    # Classify each patch individually
    results = []
    for patch in patches:
        patch_data = tf.constant(patch, dtype=tf.float32)
        patch_result = model(patch_data, training=False).numpy()
        results.append(patch_result.tolist()[0])

    # Merge the classification results for each patch into a single result
    result = sum(results) / len(results)

    # Return the final classification result
    return result
