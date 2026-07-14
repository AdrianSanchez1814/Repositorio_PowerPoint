#!/usr/bin/env python3
"""
Script to create PowerPoint presentations with mockup images
Author: Codemie
Date: 2025
"""

from pptx import Presentation
from pptx.util import Inches
from PIL import Image

def create_mockup_presentation(image_path, output_path="Customer_Success_Overview_Mockup.pptx"):
    """
    Creates a PowerPoint presentation with a mockup image
    
    Args:
        image_path: Path to the mockup image
        output_path: Output path for the PowerPoint file
    """
    
    # Create presentation object
    prs = Presentation()
    
    # Set slide dimensions to 16:9 (standard)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    # Add a blank slide
    blank_slide_layout = prs.slide_layouts[6]  # 6 is blank layout
    slide = prs.slides.add_slide(blank_slide_layout)
    
    # Get image dimensions to calculate proper sizing
    img = Image.open(image_path)
    img_width, img_height = img.size
    aspect_ratio = img_width / img_height
    
    # Calculate dimensions to fit slide
    slide_width = prs.slide_width
    slide_height = prs.slide_height
    slide_aspect_ratio = slide_width / slide_height
    
    if aspect_ratio > slide_aspect_ratio:
        # Image is wider than slide - fit to width
        pic_width = slide_width
        pic_height = int(slide_width / aspect_ratio)
        left = 0
        top = int((slide_height - pic_height) / 2)
    else:
        # Image is taller than slide - fit to height
        pic_height = slide_height
        pic_width = int(slide_height * aspect_ratio)
        left = int((slide_width - pic_width) / 2)
        top = 0
    
    # Add image to slide
    slide.shapes.add_picture(
        image_path,
        left,
        top,
        width=pic_width,
        height=pic_height
    )
    
    # Save presentation
    prs.save(output_path)
    print(f"PowerPoint presentation created successfully: {output_path}")
    
    return output_path

# Create the presentation
image_file = "V4_3.3.1.1_Customer_Success_Overview_Importe_menu.png"
output_file = create_mockup_presentation(image_file)
print(f"Presentation created: {output_file}")
