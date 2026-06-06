class Artgallery :
    def __init__(self,gallery_n,location):
        self.gallery_n = gallery_n
        self.location = location
        self.artwork = []
        print(f"\nWelcome to {self.gallery_n}!")
        print(f"Location: {self.location}")
        print("Art gallery collection is ready.")
    def add_artworks (self,artwork):
        self.artwork.append(artwork)
        print(f"'{artwork}' has been added to the gallery collection.")

    def remove_artworks(self, artwork):
        if artwork in self.artwork:
            self.artwork.remove(artwork)
            print(f"'{artwork}' has been removed from the gallery collection.")
        else:
            print(f"'{artwork}' was not found in the gallery collection.")
    
    def display_artworks(self):
        print(f"\n--- {self.gallery_n} Art Collection ---")

        if self.artworks:
            for number, artwork in enumerate(self.artworks, 1):
                print(f"{number}. {artwork}")
        else:
            print("No artworks have been added yet.")

    
    def __del__(self) :
        print(f"\nClosing {self.gallery_n}. Thank you for managing the art collection!")

gallery = Artgallery("creative works","bengaluru")

while True:
    print("\n========= ART GALLERY MENU =========")
    print("1. Add Artwork")
    print("2. Remove Artwork")
    print("3. Display Art Collection")
    print("4. Exit")
    print("===================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        artwork_name = input("Enter the artwork name to add: ")
        gallery.add_artworks(artwork_name)

    elif choice == "2":
        artwork_name = input("Enter the artwork name to remove: ")
        gallery.remove_artworks(artwork_name)

    elif choice == "3":
        gallery.display_artworks()

    elif choice == "4":
        print("Exiting the Art Gallery Collection Manager.")

        # Object Lifecycle: object deletion
        del gallery
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

    