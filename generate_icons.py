#!/usr/bin/env python3
"""Generate minimal PWA icon PNG files for S TV project."""
import struct
import zlib

def create_min_png(width, height, color=(10, 10, 20), filename):
    """Create a simple solid-color PNG file."""
    # Create RGBA buffer
    data = bytearray()
    for y in range(height):
        row = b'\x00'  # alpha padding for filter method
        for x in range(width):
            data.extend([color[0], color[1], color[2], 255])
    
    # Compress
    compressed = zlib.compress(data, 9)
    
    # Build PNG
    def chunk(t, d):
        return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xFFFFFFFF)
    
    png = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)) + \
          chunk(b'IDAT', compressed) + chunk(b'IEND', b'')
    
    with open(filename, 'wb') as f:
        f.write(png)
    print(f"Created {filename} ({width}x{height})")

# Create various sizes
create_min_png(192, 192, (0, 212, 255), 'icon-192.png')  # Cyan accent
create_min_png(512, 512, (0, 212, 255), 'icon-512.png')  # Larger version
create_min_png(180, 180, (0, 212, 255), 'apple-touch-icon.png')  # iOS
create_min_png(32, 32, (0, 212, 255), 'favicon-32.png')   # Favicon

# Create og-image.png (1200x630)
create_min_png(1200, 630, (10, 10, 20), 'og-image.png')  # Dark background

print("\nAll icon files generated successfully!")
