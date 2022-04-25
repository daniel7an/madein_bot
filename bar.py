import flag
from countries import *

def format_text(text):
    #text.replace("*", "\\*").replace("_", "\\_").replace("{", "\{").replace("}", "\}").replace("[", "\\[").replace("]", "\]").replace("(", "\(").replace(")", "\)").replace("#", "\#").replace("+", "\+").replace("-", "\-").replace(".", "\.").replace("!", "\!").replace(".", "\.")
    formated_text = text.replace(".", "\.").replace("-", "\-").replace("*", "\\*").replace("_", "\\_").replace("{", "\{").replace("}", "\}").replace("[", "\\[").replace("]", "\]").replace("(", "\(").replace(")", "\)").replace("#", "\#").replace("+", "\+").replace("!", "\!")
    return formated_text

def get_country(barcode, barcode_type):
    if barcode_type == "EAN13" and int(str(barcode)[0]) != 0:
        country_barcode = int(str(barcode)[:3])
        country_code = barcode_country(country_barcode)
        return country_code
    elif barcode_type == "EAN13" and int(str(barcode)[0]) == 0:
        country_code = ["US", "CA"]
        return country_code
    elif barcode_type == "EAN8":
        country_barcode = int(str(barcode)[:3])
        country_code = barcode_country(country_barcode)
        return country_code
    else:
        return ""
def get_from_list(counts, barcode, barcode_type, lang):
    if lang == "ru":
        text = ""

        for i in range(0, len(counts)):
            country_code = counts[i]
            country_name = get_country_name(country_code, lang)
            country_flag = flag.flag(country_code)
            
            if i == len(counts) - 1:
                text = text + country_name + " " + country_flag + "." 
            else:
                text = text + country_name + " " + country_flag + ",\n"

        result_text = f"""\u2757_Этот штрих код может принадлежать нескольких стран\._
    
*♻️ Сделано в*: {format_text(text)}

ℹ️
├ *Подлинность*: _{validity_check(barcode, barcode_type, lang)}_
├ *Штрих\-код:* _{format_text(barcode)}_
├ *Тип штрих кода*: _{barcode_type}_
├ *Код изготовителя*: _{get_company_code(barcode, barcode_type)}_
└ *Код товара*: _{get_product_code(barcode, barcode_type, lang)}_"""
        return result_text
    
    elif lang == "eng":
        text = ""

        for i in range(0, len(counts)):
            country_code = counts[i]
            country_name = get_country_name(country_code, lang)
            country_flag = flag.flag(country_code)
            
            if i == len(counts) - 1:
                text = text + country_name + " " + country_flag + "\." 
            else:
                text = text + country_name + " " + country_flag + ",\n"

        result_text = f"""\u2757_This barcode may belong to multiple countries\._

*♻️ Made in*: {text}

ℹ️
├ *Authenticity*: {validity_check(barcode, barcode_type, lang)}
├ *Barcode*: {format_text(barcode)}
├ *Barcode Type*: {barcode_type}
├ *Manufacturer Code*: {get_company_code(barcode, barcode_type)}
└ *Product Code*: {get_product_code(barcode, barcode_type, lang)}"""
        return result_text

def country_not_detected(barcode, barcode_type, lang):
    if lang == "ru":
        text = f"""*♻️ Сделано в*: Отсуствует 🚫

ℹ️
├ *Подлинность*: _{validity_check(barcode, barcode_type, lang)}_
├ *Штрих\-код:* _{format_text(barcode)}_
├ *Тип штрих кода*: _{barcode_type}_
├ *Код изготовителя*: _{get_company_code(barcode, barcode_type)}_
└ *Код товара*: _{get_product_code(barcode, barcode_type, lang)}_"""
        return text
    
    elif lang == "eng":
        text = f"""*♻️ Made in*\: Absent 🚫

ℹ️
├ *Authenticity*: _{validity_check(barcode, barcode_type, lang)}_
├ *Barcode*: _{format_text(barcode)}_
├ *Barcode Type*: _{barcode_type}_
├ *Manufacturer Code*: _{get_company_code(barcode, barcode_type)}_
└ *Product Code*: _{get_product_code(barcode, barcode_type, lang)}_""" 
        return text

def result_msg(barcode, country, barcode_type, lang):
    if lang == "ru":
        text = f"""*♻️ Сделано в:* {country}

ℹ️
├ *Подлинность*: _{validity_check(barcode, barcode_type, lang)}_
├ *Штрих\-код:* _{format_text(barcode)}_
├ *Тип штрих кода*: _{barcode_type}_
├ *Код изготовителя*: _{get_company_code(barcode, barcode_type)}_
└ *Код товара*: _{get_product_code(barcode, barcode_type, lang)}_"""
        return text
    
    elif lang == "eng":
        text = f"""*♻️ Made in:* {country}

ℹ️
├ *Authenticity*: _{validity_check(barcode, barcode_type, lang)}_
├ *Barcode*: _{format_text(barcode)}_
├ *Barcode Type*: _{barcode_type}_
├ *Manufacturer Code*: _{get_company_code(barcode, barcode_type)}_
└ *Product Code*: _{get_product_code(barcode, barcode_type, lang)}_""" 
        return text

def validity_check(code, barcode_type, lang):
    if barcode_type == "EAN13":
        contr = -1
        str_code = str(code)
        
        sum_z = 0
        sum_k = 0
        
        for i in range(0, len(str(code))):

            if (i + 1) % 2 == 0:
                sum_z = sum_z + int(str_code[i])

        for i in range(0, len(str(code)) - 1):
            if (i + 1) % 2 != 0:
                sum_k = sum_k + int(str_code[i])

        print((sum_z * 3) + sum_k)

        if ((sum_z * 3) + sum_k) % 10 == 0:
            contr = 0
        else:   
            contr = 10 - int(''.join(str((sum_z * 3) + sum_k)[-1]))
        
        if contr == int(str_code[-1]):
            if lang == "ru":
                return "Код верный ✅"
            elif lang == "eng":
                return "The code is correct ✅"
        else:
            if lang == "ru":
                return "Код неверный ❌"
            elif lang == "eng":
                return "The code is incorrect ❌"

    
    elif barcode_type == "EAN8":
        str_code = str(code)

        sum_z = 0
        sum_k = 0

        for i in range(0, len(str(code)) - 1):

            if (i + 1) % 2 == 0:
                sum_z = sum_z + int(str_code[i])

        for i in range(0, len(str(code))):
            if (i + 1) % 2 != 0:
                sum_k = sum_k + int(str_code[i])

        contr = int((str((sum_k * 3) + sum_z)))
        tasnyak = str(int(str(contr)[0]) + 1) + "0"

        result = int(tasnyak) - contr

        if result == int(str_code[-1]):
            if lang == "ru":
                return "Код верный ✅"
            elif lang == "eng":
                return "The code is correct ✅"
        else:
            if lang == "ru":
                return "Код неверный ❌"
            elif lang == "eng":
                return "The code is incorrect ❌"
    else:
        if lang == "ru":
            return "Не проверен ⚠️"
        elif lang == "eng":
            return "Not verified ⚠️"

def get_company_code(code, barcode_type):
    if barcode_type == "EAN13" and int(str(code)[0]) != 0:
        company_code = str(code[3:7])
        return company_code
    elif barcode_type == "EAN13" and int(str(code)[0]) == 0:
        company_code = str(code)[2:7]
        return company_code
    elif barcode_type == "EAN8":
        company_code = str(code[3:7])
        return company_code

def get_product_code(code, barcode_type, lang):
    if barcode_type == "EAN13" and int(str(code)[0]) != 0:
        product_code = str(code[7:12])
    elif barcode_type == "EAN13" and int(str(code)[0]) == 0:
        product_code = str(code[7:12])
    else:
        if lang == "ru":
            product_code = "Отсутствует 🚫"
        elif lang == "eng":
            product_code = "Absent 🚫"
    return product_code



info_ru = """❓ *Как пользовоться ботом*:

Пришлите мне фотографию, и я сделаю все возможное, чтобы расшифровать ее\. Код на изображении должен быть разборчив и центрирован, не должен быть расплывчатым или слишком маленьким и не плохого качества\. Кроме того, я могу декодировать только эти форматы\:

_\- 1D продукт\: UPC\-A, UPC\-E, EAN\-8, EAN\-13_
_\- 2D: QR Code_

*Примечание\:* _Бот может иногда указывать страну, в которой находится главный офис компании\._"""

info_eng = """❓ *How to use the bot*:

Send me a photo and I will do my best to decipher it\.  The code in the image should be legible and centered, not vague or too small or of poor quality\.  Also, I can only decode these formats\:

 _\-1D product\: UPC\-A, UPC\-E, EAN\-8, EAN\-13_
 _\- 2D: QR Code_

*Note\: * _Bot may sometimes indicate the country in which the company's headquarters are located\._"""