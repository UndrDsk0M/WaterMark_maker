from PIL import ImageFilter, Image


def watemarker(
    img_path="image.jpg", save_image=True, resualt_path="resualt", resualt_format="png"
) -> dict:
    """It is very simple function to use but i wiil give ome tips too :
    1. cuase i return an pillow image object to by using save_image ypu can choose to save image or just using pillow image object
    2. by defualt resualt save in : (./resualt.png)
    3. you can change this by write : watermarker(
                                    img_path="image.jpg",
                                    resualt_path="downloaded_image",
                                    resualt_format="jpeg")
    4. this function return you an dict ,
        the dict have :
            status (True/False) # if it return false it didnt work (XD just an joke)
            path the resualt image saved (if save_image equal true)
            an pillow image object (you can save it in simple varible :
                        x = watemarker("image.jpg", False)
                        image = x["the_image"]
                        image.show()
    """

    def redtangle(img, is_dark):
        if is_dark:
            # image is black watermark is white
            size = (1115, 562)
            pos = (82, 79)
            wtrmrk_url = "picture/1white_watermark.png"  # white watermark

        else:
            # image is black watermark is white
            size = (1105, 564)
            pos = (87, 75)
            wtrmrk_url = "picture/1black_watermark.png"  # black watermark

        watemark = Image.open(wtrmrk_url).convert("RGBA")

        #
        img = img.resize((1280, 720))  # setting image for back
        img_blured = img.filter(ImageFilter.GaussianBlur(5))  # blur background
        img = img.resize((1100, 550))  # setting image for front
        watemark = watemark.resize(size)

        # put imgs to each other
        new_img = img_blured.copy()
        new_img.paste(img, (90, 86))
        new_img2 = new_img.copy()
        new_img2.paste(watemark, pos, mask=watemark)

        return new_img2

    def squre(img, is_dark):
        if is_dark:
            wtrmrk_url = "picture/2WhiteSquare.png"  # white watermark
        else:
            wtrmrk_url = "picture/2BlackSquare.png"  # black watermark

        watemark = Image.open(wtrmrk_url).convert("RGBA")

        #
        img = img.resize((1080, 1080))  # setting image for back
        img_blured = img.filter(ImageFilter.GaussianBlur(5))  # blur background
        img = img.resize((900, 900))  # setting image for front
        watemark = watemark.resize((900, 920))

        new_img = img_blured.copy()
        new_img.paste(img, (90, 86))
        new_img2 = new_img.copy()
        new_img2.paste(watemark, (90, 60), mask=watemark)

        return new_img2

    img = Image.open(img_path)

    # detecting color by bluring it
    blur_image = Image.open(img_path).convert("L")
    blur_image = blur_image.filter(ImageFilter.GaussianBlur(999_999_999))
    color = blur_image.getcolors(blur_image.size[0] * blur_image.size[1])
    is_dark = False

    if (color[0][1]) < 120:
        is_dark = True

    # detecting is squre or redtangle
    if img.size[0] > img.size[1]:
        bigger = img.size[0]
        smaller = img.size[1]
    else:
        bigger = img.size[1]
        smaller = img.size[0]

    print(img.size[0])
    print(img.size[1])

    if bigger - smaller <= 200:
        img = squre(img, is_dark)
    else:
        img = redtangle(img, is_dark)

    # saving and returning resualt
    if save_image:
        img.save(f"{resualt_path}.{resualt_format}")
        return {
            "status": True,
            "path": f"{resualt_path}.{resualt_format}",
            "the_image": img,
        }
    else:
        return {"status": True, "path": None, "the_image": img}


(watemarker("x2.png")["the_image"]).show()

# By @UndrDskM
# Ehsan vakil yazdi
# ( Bot coding by @amiroim )
