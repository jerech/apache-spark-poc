import random
import string
from constants import KEY_WORD, FILE_NAME, FILE_SIZE_MB

def generate_random_text(size):
    characters = string.ascii_letters + string.digits + string.punctuation + ' '

    random_text = ''.join(random.choice(characters) for _ in range(size))
    return add_key_word(random_text)

def add_key_word(random_text):
    
    split = random_text.split(' ')
    for i in range(len(split)):
        if len(split[i]) == len(KEY_WORD):
            split[i] = KEY_WORD
    return ' '.join(split)

def write_to_file(file_path, size_mb):
    size_bytes = size_mb * 1024 * 1024
    chunk_size = 1024 * 100  # 1 MB chunk size

    with open(file_path, 'w') as f:
        while size_bytes > 0:
            if size_bytes >= chunk_size:
                chunk = generate_random_text(chunk_size)
                f.write(chunk + "\n")
                size_bytes -= chunk_size
            else:
                chunk = generate_random_text(size_bytes)
                f.write(chunk)
                size_bytes = 0

if __name__ == "__main__":
    file_path = FILE_NAME
    size_mb = FILE_SIZE_MB
    write_to_file(file_path, size_mb)
    print(f"Archivo '{file_path}' generado exitosamente con un tamaño aproximado de {size_mb} MB.")
