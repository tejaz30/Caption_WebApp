import os
import uuid
from flask import Flask, render_template, request, send_from_directory
from PIL import Image
import torch
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer

# --- Initialize Flask app ---
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# --- Load model and processor ---
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# --- Caption Generation ---
def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    pixel_values = inputs["pixel_values"].to(device)
    output_ids = model.generate(pixel_values, max_new_tokens=16)
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return caption

# --- Home Page Route ---
@app.route("/", methods=["GET", "POST"])
def index():
    caption = None
    image_path = None

    if request.method == "POST":
        if "image" not in request.files:
            return "No file part"
        file = request.files["image"]
        if file.filename == "":
            return "No selected file"
        if file:
            # Generate a unique filename to avoid overwriting
            unique_name = f"{uuid.uuid4().hex}_{file.filename}"
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], unique_name)
            file.save(save_path)

            # Generate caption
            caption = generate_caption(save_path)

            # Save caption log for gallery
            with open("gallery_log.txt", "a") as log_file:
                log_file.write(f"{unique_name}||{caption}\n")

            image_path = f"/uploads/{unique_name}"

    # Load gallery items (show most recent 6)
    gallery = []
    if os.path.exists("gallery_log.txt"):
        with open("gallery_log.txt", "r") as log_file:
            for line in reversed(log_file.readlines()):
                fname, cap = line.strip().split("||")
                gallery.append({"image": f"/uploads/{fname}", "caption": cap})
                if len(gallery) == 6:
                    break

    return render_template("index.html", caption=caption, image_path=image_path, gallery=gallery)

# --- Serve uploaded images ---
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# --- Run the app ---
if __name__ == "__main__":
    app.run(host= "0.0.0.0",port = 7860, debug=True)
