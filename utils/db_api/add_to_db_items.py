import asyncio

from utils.db_api.database import create_db, db
from utils.db_api.menu_commands import add_item


async def add_items():
    # await db.gino.drop_all()
    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Классика", category_code="Cl",
                   subcategory_name="Эспрессо", subcategory_code="Es",
                   volume="60", adds="молоко, сироп, другое",
                   price=1, photo="https://avatars.mds.yandex.net/get-zen_doc/3769362/pub_5ef14d85886c2d40a519517a_5ef14ef27fff20485b95bc10/scale_1200")

    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Классика", category_code="Cl",
                   subcategory_name="Американо", subcategory_code="Am",
                   volume="300, 200", adds="объем, молоко, сироп, другое",
                   price=1, photo="https://profnapitok.ru/wp-content/uploads/2021/09/amerikano.jpg")

    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Классика", category_code="Cl",
                   subcategory_name="Флет-Уайт", subcategory_code="Fl",
                   volume="200", adds="молоко, сироп, другое",
                   price=1, photo="https://thecoffeevine.com/wp-content/uploads/2013/10/img_5753.jpg")

    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Классика", category_code="Cl",
                   subcategory_name="Капучино", subcategory_code="Ca",
                   volume="300, 200, 400", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://phonoteka.org/uploads/posts/2021-05/1621548307_9-phonoteka_org-p-kapuchino-fon-17.jpg")

    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Классика", category_code="Cl",
                   subcategory_name="Латте", subcategory_code="La",
                   volume="300, 400", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://www.firestock.ru/download/s/inur9hlr9mygykr/firestock_latte_30072013.jpg")

    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Классика", category_code="Cl",
                   subcategory_name="Фильтр", subcategory_code="Fl",
                   volume="200", adds="молоко, сироп, другое", price=1,
                   photo="https://ae01.alicdn.com/kf/H4281ae6a98254f47843a13ae0dc5888f7/-.jpg_q50.jpg")

    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Классика", category_code="Cl",
                   subcategory_name="Воронка V60", subcategory_code="V6",
                   volume="200", adds="молоко, сироп, другое", price=1,
                   photo="https://im0-tub-ru.yandex.net/i?id=d65d0123d2ad6da87857c48b85dd6a87-l&n=13")


    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Раф", category_code="Ra",
                   subcategory_name="Арахисовый", subcategory_code="Ar",
                   volume="300, 400", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://okoffe.ru/wp-content/uploads/2021/02/2-1024x1024.png")

    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Раф", category_code="Ra",
                   subcategory_name="Ванильный", subcategory_code="Va",
                   volume="300, 400", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://okoffe.ru/wp-content/uploads/2021/02/2-1024x1024.png")

    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Раф", category_code="Ra",
                   subcategory_name="Шоколадный", subcategory_code="Ch",
                   volume="300, 400", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://okoffe.ru/wp-content/uploads/2021/02/2-1024x1024.png")

    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Холодный кофе", category_code="Cc",
                   subcategory_name="Фраппе", subcategory_code="Fr",
                   volume="500", adds="молоко, сироп, другое", price=1,
                   photo="https://cooking-24.ru/wp-content/uploads/2020/09/2-35.jpg")

    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Холодный кофе", category_code="Cc",
                   subcategory_name="Тоник", subcategory_code="To",
                   volume="400, 500", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://shop.tastycoffee.ru/files/shares/data/blog/espresso-tonic/image5.jpg")

    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Холодный кофе", category_code="Cc",
                   subcategory_name="Гляссе", subcategory_code="Gl",
                   volume="400, 500", adds="объем, молоко, сироп, другое",price=1,
                   photo="https://about-tea.ru/wp-content/uploads/5/9/b/59bd8c58f8ee4aa543a3c2db069d1281.jpeg")

    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Холодный кофе", category_code="Cc",
                   subcategory_name="Айс-латте", subcategory_code="Il",
                   volume="400, 500", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://thriftymommaramblings.com/wp-content/uploads/2017/08/Coffee-Flavors-.jpg")

    await add_item(main_name="Кофе", main_code="1_C",
                   category_name="Авторский", category_code="Au",
                   subcategory_name="Авторский кофе", subcategory_code="Ac",
                   volume="200", adds="молоко, сироп, другое", price=1,
                   photo="https://teaorcoffee.ru/wp-content/uploads/2019/10/coffe_category.jpg")


    await add_item(main_name="Напитки", main_code="3_D",
                   category_name="Не кофе", category_code="Nc",
                   subcategory_name="Какао", subcategory_code="Ka",
                   volume="300", adds="молоко, сироп, другое", price=1,
                   photo="https://chocosite.ru/wp-content/uploads/2019/11/66b0cdfa3f3db842944a1eeb5ad782c4-1024x683.jpg")

    await add_item(main_name="Напитки", main_code="3_D",
                   category_name="Не кофе", category_code="Nc",
                   subcategory_name="Горячий шоколад", subcategory_code="Hc",
                   volume="300", adds="молоко, сироп, другое", price=1,
                   photo="https://candiland.ru/wp-content/uploads/2018/04/3744x2603_814228_www.ArtFile.ru_.jpg")

    await add_item(main_name="Напитки", main_code="3_D",
                   category_name="Смузи", category_code="Sm",
                   subcategory_name="Клубника-банан", subcategory_code="Sb",
                   volume="400, 500", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://pitaniedetok.ru/wp-content/uploads/2021/09/smuzi-dlya-detey.jpg")

    await add_item(main_name="Напитки", main_code="3_D",
                   category_name="Смузи", category_code="Sm",
                   subcategory_name="Ягодный", subcategory_code="Be",
                   volume="400, 500", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://pitaniedetok.ru/wp-content/uploads/2021/09/smuzi-dlya-detey.jpg")


    await add_item(main_name="Напитки", main_code="3_D",
                   category_name="Молочный коктейль", category_code="Mc",
                   subcategory_name="Ванильный", subcategory_code="Vn",
                   volume="400, 500", adds="объем, молоко, сироп, другое", price=1,
                   photo="http://www.amati31.ru/media/cache/1d/c8/1dc8507e5b7ee9df4d8060660bfb11e6.jpg")

    await add_item(main_name="Напитки", main_code="3_D",
                   category_name="Молочный коктейль", category_code="Mc",
                   subcategory_name="Шоколад-банан", subcategory_code="Chocolate-banana",
                   volume="400, 500", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://medaboutme.ru/upload/medialibrary/e18/depositphotos_70928419_m_2015.jpg")

    await add_item(main_name="Напитки", main_code="3_D",
                   category_name="Молочный коктейль", category_code="Mc",
                   subcategory_name="Клубничный", subcategory_code="St",
                   volume="400, 500", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://img.youscreen.ru/wall/14977950232496/14977950232496_1920x1200.jpg")

    await add_item(main_name="Напитки", main_code="3_D",
                   category_name="Молочный коктейль", category_code="Mc",
                   subcategory_name="Орео", subcategory_code="Or",
                   volume="400, 500", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://i.pinimg.com/originals/49/8b/1b/498b1bf417065b0a332122b3e0a9c353.jpg")

    await add_item(main_name="Чай", main_code="2_T",
                   category_name="Чай черный", category_code="Bt",
                   subcategory_name="Пуэр", subcategory_code="Pu",
                   volume="300, 400", adds="объем, молоко, сироп, другое", price=1,
                   photo="http://g02.a.alicdn.com/kf/UT8sjqEXcldXXagOFbXY/206129557/UT8sjqEXcldXXagOFbXY.jpg")

    await add_item(main_name="Чай", main_code="2_T",
                   category_name="Чай черный", category_code="Bt",
                   subcategory_name="Ассам", subcategory_code="As",
                   volume="300, 400", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://shop.rusteaco.ru/upload/iblock/5a5/5a50a8691fd518ec7b703cda163a0924.jpg")

    await add_item(main_name="Чай", main_code="2_T",
                   category_name="Чай зеленый", category_code="Gt",
                   subcategory_name="Тегуанинь", subcategory_code="Teg",
                   volume="300, 400", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://www.solidrop.net/photo-4/organic-high-mountain-anxi-tieguanyin-tea-500g-fresh-china-green-tikuanyin-tea-oolong-tie-guan-yin.jpg")

    await add_item(main_name="Чай", main_code="2_T",
                   category_name="Чай зеленый", category_code="Gt",
                   subcategory_name="Молочный улун", subcategory_code="Mu",
                   volume="300, 400", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://cdn1.ozone.ru/s3/multimedia-h/6065030237.jpg")

    await add_item(main_name="Чай", main_code="2_T",
                   category_name="Чай зеленый", category_code="Gt",
                   subcategory_name="МолиХуаЧа", subcategory_code="Mo",
                   volume="300, 400", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://sun-tea.org/wa-data/public/shop/products/39/01/139/images/74/74.970.jpg")

    await add_item(main_name="Чай", main_code="2_T",
                   category_name="Чай фруктовый", category_code="Ft",
                   subcategory_name="Каскара", subcategory_code="Ka",
                   volume="300", adds="молоко, сироп, другое", price=1,
                   photo="http://cdn.newsdaily.org.ua/images/7971/7971-84-1539165992.jpg")
    await add_item(main_name="Чай", main_code="2_T",
                   category_name="Чай фруктовый", category_code="Ft",
                   subcategory_name="Облепиховый", subcategory_code="Bu",
                   volume="300", adds="молоко, сироп, другое", price=1,
                   photo="https://poleznii-site.ru/wp-content/uploads/2018/12/7-42.jpg")
    await add_item(main_name="Чай", main_code="2_T",
                   category_name="Чай фруктовый", category_code="Ft",
                   subcategory_name="Дерзкий фрукт", subcategory_code="Ch",
                   volume="300, 400", adds="объем, молоко, сироп, другое", price=1,
                   photo="https://img5.goodfon.ru/wallpaper/nbig/7/7e/chai-chainik-frukty-limon-miata.jpg")

    await add_item(main_name="Чай", main_code="2_T",
                   category_name="Матча/ice-матча", category_code="Ma",
                   subcategory_name="Матча-латте", subcategory_code="Ml",
                   volume="300", adds="молоко, сироп, другое", price=1,
                   photo="https://i.pinimg.com/originals/92/fd/12/92fd122ef1b4e64406801d88bbc3c690.jpg")
    await add_item(main_name="Чай", main_code="2_T",
                   category_name="Матча/ice-матча", category_code="Ma",
                   subcategory_name="Лунная ночь", subcategory_code="Mn",
                   volume="300", adds="молоко, сироп, другое", price=1,
                   photo="https://reddragontea.ru/upload/images/blog/in_article_a1a8a716ad.jpg")
    await add_item(main_name="Чай", main_code="2_T",
                   category_name="Матча/ice-матча", category_code="Ma",
                   subcategory_name="Амчур матча", subcategory_code="Am",
                   volume="300", adds="молоко, сироп, другое", price=1,
                   photo="https://sun9-58.userapi.com/impf/c844721/v844721548/b5583/5dahFdJzFTs.jpg?size=604x604&quality=96&sign=42eef62e489aeffa36e58efa12def852&type=album")
    await add_item(main_name="Чай", main_code="2_T",
                   category_name="Матча/ice-матча", category_code="Ma",
                   subcategory_name="Клубничная", subcategory_code="St",
                   volume="300", adds="молоко, сироп, другое", price=1,
                   photo="https://im0-tub-ru.yandex.net/i?id=a99491eed1004d0c8aaa69656f52026e-l&n=13")


    await add_item(main_name="Еда", main_code="4_F",
                   category_name="Вкусняшки", category_code="De",
                   subcategory_name="Гранола", subcategory_code="Gr",
                   volume="порция", adds="молоко, сироп, другое", price=1,
                   photo="https://zasushim.ru/wp-content/uploads/2020/01/4-10.jpg")
    await add_item(main_name="Еда", main_code="4_F",
                   category_name="Наборы", category_code="Se",
                   subcategory_name="Сырники & Кофе 0.3", subcategory_code="Chc",
                   volume="порция", adds="другое", price=1,
                   photo="https://img4.goodfon.ru/original/1440x900/3/a5/syrniki-kofe-dzhem-klubnika.jpg")
    await add_item(main_name="Еда", main_code="4_F",
                   category_name="Вкусняшки", category_code="De",
                   subcategory_name="Мороженое", subcategory_code="Ic",
                   volume="100", adds="сироп, другое", price=1,
                   photo="https://jam-bakery.ru/wp-content/uploads/0/5/c/05c2a71a3fb3196ae1c24248e69ef9fe.jpg")


loop = asyncio.get_event_loop()
loop.run_until_complete(create_db())
loop.run_until_complete(add_items())

