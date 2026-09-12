'''import pygame
import random
import sys
import numpy as np

# 1. Initialize Pygame
pygame.init()

# Load the target image
# Place your 'mona_lisa_small.jpg' in the same folder as this script
try:
    TARGET_IMAGE = pygame.image.load("mona_lisa_small.jpg")
except pygame.error:
    print("Error: Could not find 'mona_lisa_small.jpg'. Please place an image with this name in the same folder.")
    pygame.quit()
    sys.exit()

WIDTH, HEIGHT = TARGET_IMAGE.get_size()

# Set up the window (Target image on the left, GA reconstruction on the right)
# We add a 20-pixel divider gap between the two images
screen = pygame.display.set_mode((WIDTH * 2 + 20, HEIGHT))
pygame.display.set_caption("Genetic Algorithm Live Image Reconstruction")

# Create the canvas for our evolving "best" candidate (starts completely black)
current_best_surface = pygame.Surface((WIDTH, HEIGHT))
current_best_surface.fill((0, 0, 0))

# Variables to track statistics
generation = 0
running = True

# 2. Main Simulation Loop
while running:
    # Handle window events so the application doesn't freeze/crash
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # --- GA STEP: MUTATION ---
    # Create a copy of our current best image to mutate
    mutated_surface = current_best_surface.copy()
    
    # Generate a random brush stroke (a semi-transparent circle)
    rand_x = random.randint(0, WIDTH)
    rand_y = random.randint(0, HEIGHT)
    rand_radius = random.randint(5, 30) # Restrict size so it builds detail over time
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    rand_alpha = random.randint(20, 120) # Transparency level
    
    # To draw with transparency (alpha) in Pygame, we must use a temporary surface
    temp_shape_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.circle(temp_shape_surf, (*rand_color, rand_alpha), (rand_x, rand_y), rand_radius)
    mutated_surface.blit(temp_shape_surf, (0, 0))

    # --- GA STEP: SELECTION (FITNESS ASSESSMENT) ---
    # Safely lock surfaces and extract pixel arrays for mathematical comparison
    target_pixels = pygame.surfarray.pixels3d(TARGET_IMAGE)
    mutated_pixels = pygame.surfarray.pixels3d(mutated_surface)
    current_pixels = pygame.surfarray.pixels3d(current_best_surface)
    
    # Performance Optimization: Calculate Mean Squared Error (MSE) using every 4th pixel [::4, ::4].
    # This prevents the CPU from bottlenecking while giving plenty of detail to render.
    loss_mutated = np.mean((target_pixels[::4, ::4] - mutated_pixels[::4, ::4]) ** 2)
    loss_current = np.mean((target_pixels[::4, ::4] - current_pixels[::4, ::4]) ** 2)
    
    # CRITICAL FIX: Explicitly delete array references to UNLOCK the surfaces before blitting
    del target_pixels
    del mutated_pixels
    del current_pixels

    # If the mutation brought us closer to the target image (lower loss), accept it!
    if loss_mutated < loss_current:
        current_best_surface = mutated_surface
        current_loss = loss_mutated
    else:
        current_loss = loss_current
        
    generation += 1

    # --- RENDERING STEP ---
    # Clear background with a dark gray color
    screen.fill((40, 40, 40)) 
    
    # Draw original target image on the left half
    screen.blit(TARGET_IMAGE, (0, 0))
    
    # Draw current evolving candidate on the right half
    screen.blit(current_best_surface, (WIDTH + 20, 0))
    
    # Update window title with progress statistics every 10 generations
    if generation % 10 == 0:
        pygame.display.set_caption(f"GA Progress | Gen: {generation} | Current Error: {int(current_loss)}")

    # Update the display visually
    pygame.display.flip()'''
    
import pygame
import random
import sys
import numpy as np
import cv2

'''# 1. Initialize Pygame
pygame.init()

# Load the target image
try:
    TARGET_IMAGE = pygame.image.load("mona_lisa_small.jpg")
except pygame.error:
    print("Error: Could not find 'mona_lisa_small.jpg'. Please place your image in the same folder.")
    pygame.quit()
    sys.exit()

WIDTH, HEIGHT = TARGET_IMAGE.get_size()

# Set up display window (Target on left, GA canvas on right)
screen = pygame.display.set_mode((WIDTH * 2 + 20, HEIGHT))
pygame.display.set_caption("Optimized GA Image Reconstruction")

# Create the canvas for our evolving artwork
current_best_surface = pygame.Surface((WIDTH, HEIGHT))
current_best_surface.fill((0, 0, 0)) # Start completely black

# Variables for statistics and optimization
generation = 0
current_loss = float('inf')
running = True

# Cache target pixels as a numpy array once to prevent repeated locking overhead
target_pixels_static = pygame.surfarray.array3d(TARGET_IMAGE)

# 2. Main Evolution Loop
while running:
    # Handle OS window events so the window doesn't freeze
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # --- OPTIMIZATION 1: DYNAMIC RADIUS SCALING ---
    # Adjust shape sizes depending on how far along we are.
    # This simulates rough background painting first, moving to fine detail later.
    if generation < 15000:
        min_r, max_r = 15, 40   # Large blocks of color
        alpha_range = (10, 50)  # Faint transparent layers build smooth gradients
    elif generation < 50000:
        min_r, max_r = 5, 20    # Medium defining shapes
        alpha_range = (20, 80)
    else:
        min_r, max_r = 2, 8     # Tiny brush strokes for fine details (eyes, mouth)
        alpha_range = (30, 100)

    # --- GA STEP: MUTATION ---
    mutated_surface = current_best_surface.copy()
    
    rand_x = random.randint(0, WIDTH)
    rand_y = random.randint(0, HEIGHT)
    rand_radius = random.randint(min_r, max_r)
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    rand_alpha = random.randint(*alpha_range)
    
    # Draw transparency using a dedicated alpha surface
    temp_shape_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.circle(temp_shape_surf, (*rand_color, rand_alpha), (rand_x, rand_y), rand_radius)
    mutated_surface.blit(temp_shape_surf, (0, 0))

    # --- GA STEP: SELECTION ---
    # Read the mutated image pixels
    mutated_pixels = pygame.surfarray.pixels3d(mutated_surface)
    
    # Performance Check: Step by 4 pixels [::4, ::4] to drastically cut down mathematical calculation
    loss_mutated = np.mean((target_pixels_static[::4, ::4] - mutated_pixels[::4, ::4]) ** 2)
    
    # Crucial: Safely unlock the mutated surface
    del mutated_pixels

    # If the mutation reduces overall error (Loss), save it as the new best baseline
    if generation == 0:
        # Establish base loss on the very first frame
        current_pixels = pygame.surfarray.pixels3d(current_best_surface)
        current_loss = np.mean((target_pixels_static[::4, ::4] - current_pixels[::4, ::4]) ** 2)
        del current_pixels

    if loss_mutated < current_loss:
        current_best_surface = mutated_surface
        current_loss = loss_mutated
        
    generation += 1

    # --- OPTIMIZATION 2: BATCH RENDERING ---
    # Instead of updating your display monitor on every single mutation check,
    # we render the graphics window only once every 50 generations.
    if generation % 50 == 0:
        screen.fill((40, 40, 40)) 
        
        # Display images
        screen.blit(TARGET_IMAGE, (0, 0))
        screen.blit(current_best_surface, (WIDTH + 20, 0))
        
        # Update progress stats in window title bar
        pygame.display.set_caption(f"Gen: {generation} | Active Radius: {min_r}-{max_r}px | Error: {int(current_loss)}")
        
        # Push frame changes to monitor
        pygame.display.flip()'''
import cv2
import numpy as np

def create_molten_gold_sculpture(image_path, output_path="Compan.jpg"):
    # 1. Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not load image.")
        return

    # 2. Smooth the image to get fluid, continuous contours (molten look)
    # Using Bilateral Filter to preserve sharp edges while smoothing flat areas
    smoothed = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
    
    # 3. Convert to grayscale to use as a height/depth map
    gray = cv2.cvtColor(smoothed, cv2.COLOR_BGR2GRAY)
    
    # Apply an extra Gaussian blur to soften the heightmap transitions
    gray_blurred = cv2.GaussianBlur(gray, (5, 5),0)
    
    # 4. Calculate gradients (Sobel filters) to find surface normals/slopes
    # This simulates how the "molten liquid" curves in 3D space
    kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)
    
    gx = cv2.filter2D(gray_blurred, cv2.CV_32F, kx)
    gy = cv2.filter2D(gray_blurred, cv2.CV_32F, ky)
    
    # 5. Define a virtual light source direction (X, Y, Z)
    # Adjusting these changes where the "shine" and shadows fall
    light_dir = np.array([1.0, -1.0, 1.5], dtype=np.float32)
    light_dir /= np.linalg.norm(light_dir) # Normalize light vector
    
    # 6. Compute Surface Normals for every pixel
    # The flatter the area, the more it points "out" of the screen (Z axis)
    depth_scale = 20.0  # Increase for more dramatic 3D extrusion effect
    nx = -gx
    ny = -gy
    nz = np.full_like(gx, depth_scale)
    
    # Normalize the surface normals
    norm = np.sqrt(nx**2 + ny**2 + nz**2)
    nx /= norm
    ny /= norm
    nz /= norm
    
    # 7. Calculate Diffuse Light (Dot product of Normal and Light direction)
    # This determines how brightly lit a slope is
    intensity = nx * light_dir[0] + ny * light_dir[1] + nz * light_dir[2]
    intensity = np.clip(intensity, 0, 1)
    
    # 8. Add Specular Highlights (The "Glossy/Chrome" molten shine)
    # Shifting intensity to higher powers creates sharper metallic reflections
    specular = np.power(intensity, 8) 
    
    # 9. Color Mapping (Applying the Gold Palette)
    # Gold is characterized by deep bronze shadows, bright orange-gold midtones, and white-hot highlights
    gold_base = np.array([20, 120, 220], dtype=np.float32)    # Warm rich gold (BGR)
    gold_shadow = np.array([5, 40, 90], dtype=np.float32)     # Dark bronze/brown (BGR)
    
    # Blend base and shadow using intensity map
    sculpture = np.zeros_like(img, dtype=np.float32)
    for c in range(3): # Loop through B, G, R channels
        # Linear interpolation between shadow and base gold
        sculpture[:, :, c] = gold_shadow[c] + (gold_base[c] - gold_shadow[c]) * intensity
        
        # Add white specular shine to the highlights
        sculpture[:, :, c] += specular * 255.0
        
    # Clip values to valid image range [0, 255] and convert back to 8-bit
    sculpture = np.clip(sculpture, 0, 255).astype(np.uint8)
    
    # 10. Save and display the result
    cv2.imwrite(output_path, sculpture)
    print(f"Sculpture successfully saved to {output_path}")

# Run the function (Replace 'your_image.jpg' with your actual file path)
create_molten_gold_sculpture("Compan.jpg")

'''### How to Tweak the Look

If the result isn't quite what you visualized, you can easily modify a few parameters in the script:

* *Make it more fluid:* Increase the kernel size in cv2.GaussianBlur(gray, (5, 5), 0) to something like (15, 15). This melts away sharp details, making it look like thick, gooey liquid.
* *Make it more extruded/3D:* Lower the depth_scale value (e.g., to 5.0). Because it's a denominator in the math, a lower value amplifies the surface slope, creating sharper metallic ridges.
* *Change the lighting angle:* Alter the light_dir vector. For example, [-1.0, -1.0, 2.0] will move the light source to the top-left, altering where the gold reflections pool.
* *Make it shinier:* Increase the exponent in np.power(intensity, 8). A higher number (like 16 or 24) narrows the shiny spots, mimicking polished chrome or pristine liquid metal.'''