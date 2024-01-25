import base64
import json

def jpeg_to_binary(file_path):
    with open(file_path, "rb") as image_file:
        binary_data = base64.b64encode(image_file.read())
        return binary_data

def break_into_frames(binary_data, frame_size=1024):
    frames = []
    total_bytes = len(binary_data)

    for i in range(0, total_bytes, frame_size):
        frame = binary_data[i:i + frame_size].ljust(frame_size, b'0')
        frames.append(frame)

    return frames

def create_json(frames):
    total_frames = len(frames)

    json_data_list = []
    for i, frame in enumerate(frames):
        json_data = {
            "totalFrames": [total_frames],
            "thisFrame": [i],
            "binary": [frame.decode('utf-8')],
            "expectMore": ["true" if i < total_frames - 1 else "false"]
        }
        json_data_list.append(json_data)

    return json_data_list

image_path = 'your_image.jpg'
binary_image = jpeg_to_binary(image_path)

frames = break_into_frames(binary_image)
json_data_list = create_json(frames)

for i, json_data in enumerate(json_data_list):
    print(f"JSON for Frame {i + 1}: {json.dumps(json_data)}")
