from PIL import Image, ImageDraw, ImageFont
import calendar
import os
class CriarImagem(object):
    @staticmethod
    def CriandoImage(historicoFalha, linha, ano):
        width, height = 1000, 1000
        background_color = (255, 255, 255)
        text_color = (0, 0, 0)
        font_size = 64
        font = ImageFont.truetype("arial.ttf", font_size)
        for month in range(1, 13):
            image = Image.new("RGB", (width, height), background_color)
            draw = ImageDraw.Draw(image)
            day_width = width // 7
            day_height = height // 6
            cal = calendar.monthcalendar(ano, month)
            for week in range(len(cal)):
                for day_in_week in range(len(cal[week])):
                    x = (day_in_week * day_width)
                    y = (week * day_height)
                    day_value = cal[week][day_in_week]
                    draw.rectangle([x, y, x + day_width, y + day_height], outline="black")
                    draw.text((x + 10, y + 10), str(day_value) if day_value != 0 else "", fill=text_color, font=font)
                    for caso in historicoFalha:
                        data = caso[1]
                        day, data_month, year = map(int, data.split('/'))
                        if data_month == month and year == ano and day_value == day:
                            draw.rectangle([x, y, x + day_width, y + day_height], fill="red", outline="black")
                            draw.text((x + 10, y + 10), str(day_value) if day_value != 0 else "", fill=text_color, font=font)
            directory_path = f"{linha}"
            if not os.path.exists(os.path.join("Resultado", str(linha))):
                os.makedirs(os.path.join("Resultado", str(linha)))
            if not os.path.exists("Resultado"):
                os.makedirs("Resultado")
            image.save(f"Resultado/{linha}/historico_de_falhas_de_{linha}_{ano}_{calendar.month_name[month]}.png")