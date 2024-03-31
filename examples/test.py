from imagespuller import ImageSearch

searcher = ImageSearch()

image_urls = searcher.search_images("cat", provider="google", max_pages=1)

searcher.save_images(image_urls, query="cats", dist_folder="downloaded_images")