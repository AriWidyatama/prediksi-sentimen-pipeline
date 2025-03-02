import tensorflow as tf

LABEL_KEY = "sentimen"
FEATURE_KEY = "content"
 
def transformed_name(key):
    return key + "_xf"

def preprocessing_fn(inputs):
    outputs = {}

    outputs[transformed_name(FEATURE_KEY)] = tf.strings.lower(inputs[FEATURE_KEY])

    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)
    return outputs
