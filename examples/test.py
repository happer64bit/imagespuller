from imagespuller import ImageSearch, OutputBuilder

image_search = ImageSearch()
output_builder = OutputBuilder(output_dir="./downloaded_images")

# Search for images using Google
image_urls_google = image_search.search_images("cats", provider="google")

# Save images to the output directory
output_builder.save_images(image_urls_google, query="cats")