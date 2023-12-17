from PIL import ImageDraw, ImageFont

label2color = {
    "B-HEADER": "blue",
    "B-QUESTION": "red",
    "B-ANSWER": "green",
    "I-HEADER": "blue",
    "I-QUESTION": "red",
    "I-ANSWER": "green",
    "O": "yellow"
}

# helper function to unnormalize bboxes for drawing onto the image
def unnormalize_box(bbox, width, height):
    return [
        width * (bbox[0] / 1000),
        height * (bbox[1] / 1000),
        width * (bbox[2] / 1000),
        height * (bbox[3] / 1000),
    ]

def draw_boxes(image, boxes, predictions):
  width, height = image.size
  normalizes_boxes = [unnormalize_box(box, width, height) for box in boxes]

  # draw predictions over the image
  draw = ImageDraw.Draw(image)
  font = ImageFont.load_default()
  for prediction, box in zip(predictions, normalizes_boxes):
      # if prediction == "O":
      #     continue
      draw.rectangle(box, outline="black")
      draw.rectangle(box, outline=label2color[prediction])
      draw.text((box[0] + 10, box[1] - 10), text=prediction, fill=label2color[prediction], font=font)
  return image

def displayEntities(bboxes, predictions, label_names, image):
    # get labels
    labels = [label_names[prediction] for prediction in predictions]
    return draw_boxes(image, bboxes[0], labels)