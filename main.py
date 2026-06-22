from PIL import Image
import random


def password_to_key(password):
    return sum(ord(c) for c in password)


def encrypt_image():
    image_path = input("Enter image path: ")
    password = input("Enter password: ")

    try:
        key = password_to_key(password)

        img = Image.open(image_path).convert("RGB")
        pixels = list(img.getdata())

        # RGB Transformation
        encrypted_pixels = []

        for r, g, b in pixels:
            encrypted_pixels.append((
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            ))

        # Pixel Shuffling
        random.seed(key)

        indices = list(range(len(encrypted_pixels)))
        random.shuffle(indices)

        shuffled_pixels = [None] * len(encrypted_pixels)

        for i, shuffled_index in enumerate(indices):
            shuffled_pixels[shuffled_index] = encrypted_pixels[i]

        encrypted_img = Image.new("RGB", img.size)
        encrypted_img.putdata(shuffled_pixels)

        output_file = "encrypted.png"
        encrypted_img.save(output_file)

        print("\n✅ Image encrypted successfully!")
        print(f"Saved as: {output_file}")

    except Exception as e:
        print("Error:", e)


def decrypt_image():
    image_path = input("Enter encrypted image path: ")
    password = input("Enter password: ")

    try:
        key = password_to_key(password)

        img = Image.open(image_path).convert("RGB")
        shuffled_pixels = list(img.getdata())

        # Recreate shuffle order
        random.seed(key)

        indices = list(range(len(shuffled_pixels)))
        random.shuffle(indices)

        unshuffled_pixels = [None] * len(shuffled_pixels)

        for i, shuffled_index in enumerate(indices):
            unshuffled_pixels[i] = shuffled_pixels[shuffled_index]

        # Reverse RGB Transformation
        decrypted_pixels = []

        for r, g, b in unshuffled_pixels:
            decrypted_pixels.append((
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            ))

        decrypted_img = Image.new("RGB", img.size)
        decrypted_img.putdata(decrypted_pixels)

        output_file = "decrypted.png"
        decrypted_img.save(output_file)

        print("\n✅ Image decrypted successfully!")
        print(f"Saved as: {output_file}")

    except Exception as e:
        print("Error:", e)


def main():
    while True:

        print("\n" + "=" * 35)
        print("        PIXELCRYPT 🔐")
        print("=" * 35)
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            encrypt_image()

        elif choice == "2":
            decrypt_image()

        elif choice == "3":
            print("\nThank you for using PixelCrypt!")
            break

        else:
            print("\n❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()