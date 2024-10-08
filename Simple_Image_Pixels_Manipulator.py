from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Function to encrypt the image
def encrypt_image(img_path, key):
    # Open the image
    img = Image.open(img_path)
    pixels = img.load()

    # Convert key to integer for XOR operation
    key = int(key)

    # Get image dimensions
    width, height = img.size

    # Encrypt each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Apply XOR with key
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    # Save encrypted image
    encrypted_img_path = os.path.splitext(img_path)[0] + "_encrypted.png"
    img.save(encrypted_img_path)
    return encrypted_img_path

# Function to decrypt the image
def decrypt_image(img_path, key):
    # Open the image
    img = Image.open(img_path)
    pixels = img.load()

    # Convert key to integer for XOR operation
    key = int(key)

    # Get image dimensions
    width, height = img.size

    # Decrypt each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Apply XOR with key (reverses the encryption)
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    # Save decrypted image
    decrypted_img_path = os.path.splitext(img_path)[0] + "_decrypted.png"
    img.save(decrypted_img_path)
    return decrypted_img_path

# Function to select an image file
def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img_path_entry.delete(0, tk.END)
        img_path_entry.insert(0, file_path)

# Function to handle encryption
def encrypt_action():
    img_path = img_path_entry.get()
    key = key_entry.get()

    if not img_path or not key:
        messagebox.showerror("Error", "Please provide both image path and key.")
        return

    encrypted_img = encrypt_image(img_path, key)
    messagebox.showinfo("Success", f"Image encrypted and saved as: {encrypted_img}")

# Function to handle decryption
def decrypt_action():
    img_path = img_path_entry.get()
    key = key_entry.get()

    if not img_path or not key:
        messagebox.showerror("Error", "Please provide both image path and key.")
        return

    decrypted_img = decrypt_image(img_path, key)
    messagebox.showinfo("Success", f"Image decrypted and saved as: {decrypted_img}")

# GUI Setup
root = tk.Tk()
root.title("Image Encryption Tool")
root.geometry("400x200")

# Image Path Label and Entry
img_path_label = tk.Label(root, text="Image Path:")
img_path_label.pack(pady=5)
img_path_entry = tk.Entry(root, width=50)
img_path_entry.pack(pady=5)

# Browse Button
browse_button = tk.Button(root, text="Browse", command=browse_image)
browse_button.pack(pady=5)

# Key Label and Entry
key_label = tk.Label(root, text="Encryption/Decryption Key:")
key_label.pack(pady=5)
key_entry = tk.Entry(root, width=20)
key_entry.pack(pady=5)

# Encrypt and Decrypt Buttons
encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_action)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_action)
decrypt_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
