from PIL import Image
try:
    image_1 = Image.open(r"C:\Users\evgue\OneDrive\Документы\GeekBrains\Python_version2_Oct_2021\01.jpg")
    image_2 = Image.open(r"C:\Users\evgue\OneDrive\Документы\GeekBrains\Python_version2_Oct_2021\02.jpg")
    image_3 = Image.open(r"C:\Users\evgue\OneDrive\Документы\GeekBrains\Python_version2_Oct_2021\02.jpg")
    image_4 = Image.open(r"C:\Users\evgue\OneDrive\Документы\GeekBrains\Python_version2_Oct_2021\02.jpg")
    image_5 = Image.open(r"C:\Users\evgue\OneDrive\Документы\GeekBrains\Python_version2_Oct_2021\02.jpg")
    image_6 = Image.open(r"C:\Users\evgue\OneDrive\Документы\GeekBrains\Python_version2_Oct_2021\02.jpg")
    image_7 = Image.open(r"C:\Users\evgue\OneDrive\Документы\GeekBrains\Python_version2_Oct_2021\02.jpg")
    image_8 = Image.open(r"C:\Users\evgue\OneDrive\Документы\GeekBrains\Python_version2_Oct_2021\02.jpg")
    image_9 = Image.open(r"C:\Users\evgue\OneDrive\Документы\GeekBrains\Python_version2_Oct_2021\02.jpg")
    image_1.show()
    image_2.show()
    image_3.show()
    image_4.show()
    image_5.show()
    image_6.show()
    image_7.show()
    image_8.show()
    image_9.show()

except FileNotFoundError:
    print("Файл не найден")