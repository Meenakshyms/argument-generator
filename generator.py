# generator.py
from topics import topics_dict

def generate_argument(topic, mode):
    """
    Returns pre-defined argument for a topic based on mode.
    mode: 'supportive', 'against', 'balanced'
    """
    if topic not in topics_dict:
        return "Topic not found. Please select a valid topic."

    topic_data = topics_dict[topic]
    return topic_data.get(mode, "No argument defined for this mode.")
