import os
from PIL import Image, ImageDraw, ImageFilter, ImageColor

def get_quad_bezier(p0, p1, p2, num_steps=100):
    points = []
    for i in range(num_steps + 1):
        t = i / num_steps
        x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t**2 * p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t**2 * p2[1]
        points.append((x, y))
    return points

def get_cubic_bezier(p0, p1, p2, p3, num_steps=50):
    points = []
    for i in range(num_steps + 1):
        t = i / num_steps
        x = (1-t)**3 * p0[0] + 3*(1-t)**2 * t * p1[0] + 3*(1-t)*t**2 * p2[0] + t**3 * p3[0]
        y = (1-t)**3 * p0[1] + 3*(1-t)**2 * t * p1[1] + 3*(1-t)*t**2 * p2[1] + t**3 * p3[1]
        points.append((x, y))
    return points

def generate_icon(size):
    # We render at 4x resolution and downsample to get beautiful antialiasing
    scale = 4
    render_size = size * scale
    
    # 1. Background Gradient
    # Create a 2x2 image to interpolate gradient, then resize to render_size
    grad_base = Image.new("RGBA", (2, 2))
    # Top-left cream, Bottom-right soft green-grey
    grad_base.putpixel((0, 0), ImageColor.getrgb("#FCF8F5") + (255,))
    grad_base.putpixel((1, 0), ImageColor.getrgb("#EEF2F0") + (255,))
    grad_base.putpixel((0, 1), ImageColor.getrgb("#EEF2F0") + (255,))
    grad_base.putpixel((1, 1), ImageColor.getrgb("#E2ECE7") + (255,))
    bg_grad = grad_base.resize((render_size, render_size), Image.Resampling.BILINEAR)
    
    # Create final image with background
    img = Image.new("RGBA", (render_size, render_size))
    img.paste(bg_grad)
    
    # 2. Watercolor Blobs Layer
    blobs = Image.new("RGBA", (render_size, render_size), (0, 0, 0, 0))
    blobs_draw = ImageDraw.Draw(blobs)
    
    # Soft green-blue blob
    green_cx, green_cy, green_r = 190 * scale, 220 * scale, 110 * scale
    blobs_draw.ellipse(
        [green_cx - green_r, green_cy - green_r, green_cx + green_r, green_cy + green_r],
        fill=ImageColor.getrgb("#CBE5DA") + (191,) # 75% opacity
    )
    
    # Soft blush-pink blob
    pink_cx, pink_cy, pink_r = 320 * scale, 290 * scale, 100 * scale
    blobs_draw.ellipse(
        [pink_cx - pink_r, pink_cy - pink_r, pink_cx + pink_r, pink_cy + pink_r],
        fill=ImageColor.getrgb("#F7DCD9") + (178,) # 70% opacity
    )
    
    # Apply Blur
    blobs = blobs.filter(ImageFilter.GaussianBlur(30 * scale))
    img = Image.alpha_composite(img, blobs)
    
    # 3. Card Layer (rotated slightly by 3 degrees clockwise, which is -3 in PIL rotate)
    card_layer = Image.new("RGBA", (render_size, render_size), (0, 0, 0, 0))
    card_draw = ImageDraw.Draw(card_layer)
    
    card_x1, card_y1 = 146 * scale, 126 * scale
    card_x2, card_y2 = (146 + 220) * scale, (126 + 260) * scale
    card_rx = 36 * scale
    card_stroke = 8 * scale
    
    # Outer Card Fill
    card_draw.rounded_rectangle(
        [card_x1, card_y1, card_x2, card_y2],
        radius=card_rx,
        fill=(255, 255, 255, int(255 * 0.55)), # 55% opacity white
    )
    
    # Inside lines (notes)
    line1_y = 290 * scale
    line2_y = 324 * scale
    card_draw.line(
        [(186 * scale, line1_y), (266 * scale, line1_y)],
        fill=ImageColor.getrgb("#7E6D66") + (166,), # 65% opacity
        width=6 * scale,
        joint="round"
    )
    card_draw.line(
        [(186 * scale, line2_y), (296 * scale, line2_y)],
        fill=ImageColor.getrgb("#7E6D66") + (166,), # 65% opacity
        width=6 * scale,
        joint="round"
    )
    
    # Outer Card Stroke
    card_draw.rounded_rectangle(
        [card_x1, card_y1, card_x2, card_y2],
        radius=card_rx,
        fill=None,
        outline=ImageColor.getrgb("#52433D") + (255,),
        width=card_stroke
    )
    
    # Rotate clockwise around center (256, 256) -> in PIL rotate by -3
    rotated_card = card_layer.rotate(-3, resample=Image.Resampling.BICUBIC, center=(256 * scale, 256 * scale))
    img = Image.alpha_composite(img, rotated_card)
    
    # 4. Plant Stem & Leaves Layer
    plant_layer = Image.new("RGBA", (render_size, render_size), (0, 0, 0, 0))
    plant_draw = ImageDraw.Draw(plant_layer)
    
    # Draw Stem
    stem_p0 = (230 * scale, 380 * scale)
    stem_p1 = (240 * scale, 250 * scale)
    stem_p2 = (310 * scale, 146 * scale)
    stem_points = get_quad_bezier(stem_p0, stem_p1, stem_p2)
    plant_draw.line(stem_points, fill=ImageColor.getrgb("#52433D") + (255,), width=9 * scale, joint="round")
    
    # Leaf helper to draw filled shape + stroke
    def draw_leaf(p0, p1, p2, p3, p4, p5):
        # Cubic Bezier segment 1: p0 to p3 via controls p1, p2
        seg1 = get_cubic_bezier(p0, p1, p2, p3)
        # Cubic Bezier segment 2: p3 to p0 via controls p4, p5
        seg2 = get_cubic_bezier(p3, p4, p5, p0)
        # Combine
        leaf_poly = seg1 + seg2
        # Fill leaf
        plant_draw.polygon(leaf_poly, fill=ImageColor.getrgb("#99C2AF") + (255,))
        # Outline leaf
        plant_draw.polygon(leaf_poly, fill=None, outline=ImageColor.getrgb("#52433D") + (255,), width=7 * scale)
        
    # Scale coordinates for leaf points
    # Leaf 1 (Top right)
    draw_leaf(
        (310*scale, 146*scale), (330*scale, 146*scale), (342*scale, 126*scale), (332*scale, 108*scale),
        (314*scale, 108*scale), (302*scale, 128*scale)
    )
    
    # Leaf 2 (Middle right)
    draw_leaf(
        (276*scale, 215*scale), (300*scale, 220*scale), (310*scale, 205*scale), (304*scale, 186*scale),
        (285*scale, 186*scale), (275*scale, 201*scale)
    )
    
    # Leaf 3 (Middle left)
    draw_leaf(
        (239*scale, 270*scale), (215*scale, 265*scale), (205*scale, 280*scale), (211*scale, 299*scale),
        (230*scale, 299*scale), (240*scale, 284*scale)
    )
    
    # Leaf 4 (Lower right)
    draw_leaf(
        (252*scale, 248*scale), (276*scale, 253*scale), (286*scale, 238*scale), (280*scale, 219*scale),
        (261*scale, 219*scale), (251*scale, 234*scale)
    )
    
    # Paste plant
    img = Image.alpha_composite(img, plant_layer)
    
    # 5. Medical Cross Layer
    cross_layer = Image.new("RGBA", (render_size, render_size), (0, 0, 0, 0))
    cross_draw = ImageDraw.Draw(cross_layer)
    
    # We draw the cross at (0, 0) relative to a temporary image, rotate it, and paste it.
    cross_w, cross_h = 200 * scale, 200 * scale
    temp_cross = Image.new("RGBA", (cross_w, cross_h), (0, 0, 0, 0))
    temp_draw = ImageDraw.Draw(temp_cross)
    
    cx_cx, cx_cy = cross_w // 2, cross_h // 2
    cx_rx = 4 * scale
    cx_stroke = 5 * scale
    
    # Vert rect: x=-6, y=-18, w=12, h=36
    v_x1, v_y1 = cx_cx - 6 * scale, cx_cy - 18 * scale
    v_x2, v_y2 = cx_cx + 6 * scale, cx_cy + 18 * scale
    # Horiz rect: x=-18, y=-6, w=36, h=12
    h_x1, h_y1 = cx_cx - 18 * scale, cx_cy - 6 * scale
    h_x2, h_y2 = cx_cx + 18 * scale, cx_cy + 6 * scale
    
    # Draw filled cross pieces
    temp_draw.rounded_rectangle([v_x1, v_y1, v_x2, v_y2], radius=cx_rx, fill=ImageColor.getrgb("#D39892") + (255,))
    temp_draw.rounded_rectangle([h_x1, h_y1, h_x2, h_y2], radius=cx_rx, fill=ImageColor.getrgb("#D39892") + (255,))
    
    # Draw outlines
    temp_draw.rounded_rectangle([v_x1, v_y1, v_x2, v_y2], radius=cx_rx, fill=None, outline=ImageColor.getrgb("#52433D") + (255,), width=cx_stroke)
    temp_draw.rounded_rectangle([h_x1, h_y1, h_x2, h_y2], radius=cx_rx, fill=None, outline=ImageColor.getrgb("#52433D") + (255,), width=cx_stroke)
    
    # Rotate by 5 degrees counter-clockwise (which matches -5 SVG rotate)
    rotated_temp_cross = temp_cross.rotate(5, resample=Image.Resampling.BICUBIC)
    
    # Paste onto cross_layer at center (305 * scale, 230 * scale)
    paste_x = 305 * scale - cx_cx
    paste_y = 230 * scale - cx_cy
    cross_layer.paste(rotated_temp_cross, (paste_x, paste_y), rotated_temp_cross)
    
    img = Image.alpha_composite(img, cross_layer)
    
    # 6. Apply Rounded Corner Mask to make the entire PWA icon maskable/rounded
    # Create mask at render size
    mask = Image.new("L", (render_size, render_size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, render_size, render_size], radius=116 * scale, fill=255)
    
    # Create transparent image
    final_img = Image.new("RGBA", (render_size, render_size), (0, 0, 0, 0))
    final_img.paste(img, (0, 0), mask=mask)
    
    # 7. Resize to final size using Lanczos (high quality)
    output_img = final_img.resize((size, size), Image.Resampling.LANCZOS)
    return output_img

if __name__ == "__main__":
    public_dir = "public"
    
    print("Generating pwa-icon-192.png...")
    img_192 = generate_icon(192)
    img_192.save(os.path.join(public_dir, "pwa-icon-192.png"), "PNG")
    
    print("Generating pwa-icon-512.png...")
    img_512 = generate_icon(512)
    img_512.save(os.path.join(public_dir, "pwa-icon-512.png"), "PNG")
    
    print("PWA Icons generated successfully!")
