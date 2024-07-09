import matplotlib.pyplot as plt
import numpy as np


def mandelbrot(c, max_iter):
  """
  Calculates the number of iterations required to determine if a complex number 'c' belongs to the Mandelbrot set.

  Args:
      c: A complex number represented by a tuple (real, imaginary)
      max_iter: The maximum number of iterations allowed to classify 'c' within the Mandelbrot set.

  Returns:
      The number of iterations needed to classify 'c' within the Mandelbrot set,
      or 'max_iter' if the limit is not reached.
  """
  z = c
  for n in range(max_iter):
    if abs(z) > 2.0:
      return n
    z = z * z + c
  return max_iter

# Define the image width and height
width, height = 500, 500

# Set the boundaries of the complex plane to be explored
xmin, xmax, ymin, ymax = -2.5, 1.5, -2.0, 2.0

# Create an empty array to store the iteration counts for each pixel
mandelbrot_set = np.zeros((height, width))

# Iterate over each pixel in the image
for x in range(width):
  for y in range(height):
    # Convert pixel coordinates to complex plane coordinates
    real = xmin + (x / (width - 1)) * (xmax - xmin)
    imag = ymin + (y / (height - 1)) * (ymax - ymin)
    c = complex(real, imag)

    # Calculate the number of iterations for the current pixel
    mandelbrot_set[y, x] = mandelbrot(c, max_iter=255)

# Plot the Mandelbrot set
plt.imshow(mandelbrot_set, extent=(xmin, xmax, ymin, ymax), cmap='hot')
plt.colorbar()
plt.title('Mandelbrot set')
plt.axis('off')
plt.show()
