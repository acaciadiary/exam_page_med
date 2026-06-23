import os
from PIL import Image, ImageDraw, ImageFilter, ImageColor

def get_cubic_bezier(p0, p1, p2, p3, num_steps=50):
    points = []
    for i in range(num_steps + 1):
        t = i / num_steps
        x = (1-t)**3 * p0[0] + 3*(1-t)**2 * t * p1[0] + 3*(1-t)*t**2 * p2[0] + t**3 * p3[0]
        y = (1-t)**3 * p0[1] + 3*(1-t)**2 * t * p1[1] + 3*(1-t)*t**2 * p2[1] + t**3 * p3[1]
        points.append((x, y))
    return points

def generate_icon(size):
    scale = 4
    render_size = size * scale
    
    # 1. Solid Cozy Cream-Beige Background
    img = Image.new("RGBA", (render_size, render_size), ImageColor.getrgb("#FCF6F0") + (255,))
    
    # 2. Twig Draw Layer
    twig_layer = Image.new("RGBA", (render_size, render_size), (0, 0, 0, 0))
    twig_draw = ImageDraw.Draw(twig_layer)
    
    # Absolute center translation
    cx, cy = 256, 266
    
    # Draw Stem (M -10 130 C 0 60 20 -20 60 -100 relative to cx, cy)
    stem_p0 = ((cx - 10) * scale, (cy + 130) * scale)
    stem_p1 = ((cx + 0) * scale, (cy + 60) * scale)
    stem_p2 = ((cx + 20) * scale, (cy - 20) * scale)
    stem_p3 = ((cx + 60) * scale, (cy - 100) * scale)
    stem_points = get_cubic_bezier(stem_p0, stem_p1, stem_p2, stem_p3)
    
    twig_draw.line(stem_points, fill=ImageColor.getrgb("#52433D") + (255,), width=12 * scale, joint="round")
    
    # Leaf helper
    def draw_leaf(p0, p1, p2, p3, p4, p5):
        # Convert relative coords to absolute scaled coords
        p0_abs = ((cx + p0[0]) * scale, (cy + p0[1]) * scale)
        p1_abs = ((cx + p1[0]) * scale, (cy + p1[1]) * scale)
        p2_abs = ((cx + p2[0]) * scale, (cy + p2[1]) * scale)
        p3_abs = ((cx + p3[0]) * scale, (cy + p3[1]) * scale)
        p4_abs = ((cx + p4[0]) * scale, (cy + p4[1]) * scale)
        p5_abs = ((cx + p5[0]) * scale, (cy + p5[1]) * scale)
        
        seg1 = get_cubic_bezier(p0_abs, p1_abs, p2_abs, p3_abs)
        seg2 = get_cubic_bezier(p3_abs, p4_abs, p5_abs, p0_abs)
        leaf_poly = seg1 + seg2
        
        # Fill leaf (Sage green)
        twig_draw.polygon(leaf_poly, fill=ImageColor.getrgb("#A4C7B6") + (255,))
        # Outline leaf (Cocoa brown)
        twig_draw.polygon(leaf_poly, fill=None, outline=ImageColor.getrgb("#52433D") + (255,), width=9 * scale)

    # Leaf 1 (Top)
    draw_leaf(
        (60, -100), (80, -100), (95, -125), (80, -145),
        (60, -145), (45, -120)
    )
    
    # Leaf 2 (Upper Left)
    draw_leaf(
        (32, -30), (5, -35), (-15, -10), (-5, 10),
        (20, 10), (30, -10)
    )
    
    # Leaf 3 (Upper Right)
    draw_leaf(
        (46, -65), (75, -60), (85, -85), (75, -105),
        (50, -105), (40, -80)
    )
    
    # Leaf 4 (Lower Left)
    draw_leaf(
        (12, 35), (-15, 30), (-35, 55), (-25, 75),
        (0, 75), (10, 50)
    )
    
    # Leaf 5 (Lower Right)
    draw_leaf(
        (23, 5), (50, 10), (60, -15), (50, -35),
        (25, -35), (15, -10)
    )
    
    img = Image.alpha_composite(img, twig_layer)
    
    # 3. Apply Rounded Corner Mask
    mask = Image.new("L", (render_size, render_size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, render_size, render_size], radius=116 * scale, fill=255)
    
    final_img = Image.new("RGBA", (render_size, render_size), (0, 0, 0, 0))
    final_img.paste(img, (0, 0), mask=mask)
    
    # 4. Resize to final size
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
