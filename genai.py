import fitz  # PyMuPDF

def extract_images_from_pdf(pdf_path, output_folder):
    with fitz.open(pdf_path) as pdf:
        for i, page in enumerate(pdf):
            image_list = page.get_images(full=True)
            for image_index, img in enumerate(image_list):
                xref = img[0]
                base_image = pdf.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_path = f"{output_folder}/image_{i + 1}_{image_index + 1}.{image_ext}"
                
                with open(image_path, "wb") as image_file:
                    image_file.write(image_bytes)
