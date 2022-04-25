import gettext
import pycountry

russian = gettext.translation("iso3166", pycountry.LOCALES_DIR, languages=["ru"])
russian.install()

def get_country_name(code, lang):
    country = pycountry.countries.get(alpha_2=code)
    if lang == "ru":
        return _(country.name)
    elif lang == "eng":
        return country.name


def barcode_country(code):
    if ((100 <= code and code <= 139)):
        return 'US'
    elif ((200 <= code and code <= 299)):
        return 'Ограниченное распространение (определено MO)'
    elif ((300 <= code and code <= 379)):
        return ["FR","MC"]
    elif (code == 380):
        return 'BG'
    elif (code == 383):
        return 'SI'
    elif (code == 385):
        return 'HR'
    elif (code == 387):
        return 'BA'
    elif (code == 389):
        return 'ME'
    elif ((400 <= code and code <= 440)):
        return 'DE'
    elif ((450 <= code and code <= 459)):
        return 'JP'
    elif ((460 <= code and code <= 469)):
        return 'RU'
    elif (code == 470):
        return 'KG'
    elif (code == 471):
        return 'TW'
    elif (code == 474):
        return 'EE'
    elif (code == 475):
        return 'LV'
    elif (code == 476):
        return 'AZ'
    elif (code == 477):
        return 'LT'
    elif (code == 478):
        return 'UZ'
    elif (code == 479):
        return 'LK'
    elif (code == 480):
        return 'PH'
    elif (code == 481):
        return 'BY'
    elif (code == 482):
        return 'UA'
    elif (code == 484):
        return 'MD'
    elif (code == 485):
        return 'AM'
    elif (code == 486):
        return 'GE'
    elif (code == 487):
        return 'KZ'
    elif (code == 488):
        return 'TJ'
    elif (code == 489):
        return 'HK'
    elif ((490 <= code and code <= 499)):
        return 'JP'
    elif ((500 <= code and code <= 509)):
        return 'GB'
    elif ((520 <= code and code <= 521)):
        return 'GR'
    elif (code == 528):
        return 'LB'
    elif (code == 529):
        return 'CY'
    elif (code == 530):
        return 'AL'
    elif (code == 531):
        return 'MK'
    elif (code == 535):
        return 'MT'
    elif (code == 539):
        return 'IE'
    elif ((540 <= code and code <= 549)):
        return ["BE","LU"]
    elif (code == 560):
        return 'PT'
    elif (code == 569):
        return 'IS'
    elif ((570 <= code and code <= 579)):
        return ["DK","FO","GL"]
    elif (code == 590):
        return 'PL'
    elif (code == 594):
        return 'RO'
    elif (code == 599):
        return 'HU'
    elif ((600 <= code and code <= 601)):
        return 'ZA'
    elif (code == 603):
        return 'GH'
    elif (code == 604):
        return 'SN'
    elif (code == 608):
        return 'BH'
    elif (code == 609):
        return 'MU'
    elif (code == 611):
        return 'MA'
    elif (code == 613):
        return 'DZ'
    elif (code == 615):
        return 'NG'
    elif (code == 616):
        return 'KE'
    elif (code == 618):
        return 'CI'
    elif (code == 619):
        return 'TN'
    elif (code == 621):
        return 'SY'
    elif (code == 622):
        return 'EG'
    elif (code == 624):
        return 'LY'
    elif (code == 625):
        return 'JO'
    elif (code == 626):
        return 'IR'
    elif (code == 627):
        return 'KW'
    elif (code == 628):
        return 'SA'
    elif (code == 629):
        return 'AE'
    elif ((640 <= code and code <= 649)):
        return 'FI'
    elif ((690 <= code and code <= 695)):
        return 'CN'
    elif ((700 <= code and code <= 709)):
        return 'NO'
    elif (code == 729):
        return 'IL'
    elif ((730 <= code and code <= 739)):
        return 'SE'
    elif (code == 740):
        return 'GT'
    elif (code == 741):
        return 'SV'
    elif (code == 742):
        return 'HN'
    elif (code == 743):
        return 'NI'
    elif (code == 744):
        return 'CR'
    elif (code == 745):
        return 'PA'
    elif (code == 746):
        return 'DO'
    elif (code == 750):
        return 'MX'
    elif ((754 <= code and code <= 755)):
        return 'CA'
    elif (code == 759):
        return 'VE'
    elif ((760 <= code and code <= 769)):
        return ["CH","LI"]
    elif ((770 <= code and code <= 771)):
        return 'CO'
    elif (code == 773):
        return 'UY'
    elif (code == 775):
        return 'PE'
    elif (code == 777):
        return 'BO'
    elif (code == 779):
        return 'AR'
    elif (code == 780):
        return 'CL'
    elif (code == 784):
        return 'PY'
    elif (code == 785):
        return 'PE'
    elif (code == 786):
        return 'EC'
    elif ((789 <= code and code <= 790)):
        return 'BR'
    elif ((800 <= code and code <= 839)):
        return ["IT","SM","VA"]
    elif ((840 <= code and code <= 849)):
        return ["ES","AD"]
    elif (code == 850):
        return 'CU'
    elif (code == 858):
        return 'SK'
    elif (code == 859):
        return 'CZ'
    elif (code == 860):
        return 'RS'
    elif (code == 865):
        return 'MN'
    elif (code == 867):
        return 'KP'
    elif ((868 <= code and code <= 869)):
        return 'TR'
    elif ((870 <= code and code <= 879)):
        return 'AN'
    elif (code == 880):
        return 'KR'
    elif (code == 884):
        return 'KH'
    elif (code == 885):
        return 'TH'
    elif (code == 888):
        return 'SG'
    elif (code == 890):
        return 'IN'
    elif (code == 893):
        return 'VN'
    elif (code == 896):
        return 'PK'
    elif (code == 899):
        return 'ID'
    elif ((900 <= code and code <= 919)):
        return 'AT'
    elif ((930 <= code and code <= 939)):
        return 'AU'
    elif ((940 <= code and code <= 949)):
        return 'NZ'
    elif (code == 950):
        return 'Специальные приложения для глобального офиса'
    elif (code == 951):
        return 'Специальные приложения для глобального офиса'
    elif (code == 955):
        return 'MY'
    elif (code == 958):
        return 'MO'
    elif ((960 <= code and code <= 969)):
        return 'GS1 Глобальный офис: GTIN\-8 распределения'
    elif (code == 977):
        return 'Серийные публикации \(ISSN\)'
    elif ((978 <= code and code <= 979)):
        return 'Bookland \(ISBN\) используется для нот'
    elif (code == 980):
        return 'Квитанции о возмещении'
    elif ((981 <= code and code <= 983)):
        return 'Купоны в единой валюте'
    elif ((990 <= code and code <= 999)):
        return 'Купоны'
    else:
        return 'not detected'
