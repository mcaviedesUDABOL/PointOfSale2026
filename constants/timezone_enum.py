from enum import Enum
from typing import List, Dict, Optional

class Timezone(Enum):
    """Enumerador con todas las zonas horarias del mundo"""
    
    # UTC
    UTC = "UTC"
    
    # Europa
    EUROPE_LONDON = "Europe/London"
    EUROPE_DUBLIN = "Europe/Dublin"
    EUROPE_LISBON = "Europe/Lisbon"
    EUROPE_MADRID = "Europe/Madrid"
    EUROPE_BARCELONA = "Europe/Barcelona"  # Aunque no es oficial, a veces se usa
    EUROPE_PARIS = "Europe/Paris"
    EUROPE_BERLIN = "Europe/Berlin"
    EUROPE_ROME = "Europe/Rome"
    EUROPE_AMSTERDAM = "Europe/Amsterdam"
    EUROPE_BRUSSELS = "Europe/Brussels"
    EUROPE_VIENNA = "Europe/Vienna"
    EUROPE_ZURICH = "Europe/Zurich"
    EUROPE_STOCKHOLM = "Europe/Stockholm"
    EUROPE_COPENHAGEN = "Europe/Copenhagen"
    EUROPE_OSLO = "Europe/Oslo"
    EUROPE_HELSINKI = "Europe/Helsinki"
    EUROPE_ATHENS = "Europe/Athens"  # Grecia
    EUROPE_ISTANBUL = "Europe/Istanbul"
    EUROPE_MOSCOW = "Europe/Moscow"
    EUROPE_WARSAW = "Europe/Warsaw"
    EUROPE_PRAGUE = "Europe/Prague"
    EUROPE_BUDAPEST = "Europe/Budapest"
    EUROPE_BUCHAREST = "Europe/Bucharest"
    EUROPE_SOFIA = "Europe/Sofia"
    EUROPE_KIEV = "Europe/Kiev"
    EUROPE_MINSK = "Europe/Minsk"
    
    # América del Norte
    AMERICA_NEW_YORK = "America/New_York"
    AMERICA_LOS_ANGELES = "America/Los_Angeles"
    AMERICA_CHICAGO = "America/Chicago"
    AMERICA_DENVER = "America/Denver"
    AMERICA_PHOENIX = "America/Phoenix"
    AMERICA_ANCHORAGE = "America/Anchorage"
    AMERICA_HONOLULU = "America/Honolulu"
    AMERICA_TORONTO = "America/Toronto"
    AMERICA_VANCOUVER = "America/Vancouver"
    AMERICA_MONTREAL = "America/Montreal"
    AMERICA_MEXICO_CITY = "America/Mexico_City"
    AMERICA_TIJUANA = "America/Tijuana"
    AMERICA_GUATEMALA = "America/Guatemala"
    AMERICA_MANAGUA = "America/Managua"
    AMERICA_TEGUCIGALPA = "America/Tegucigalpa"
    AMERICA_SAN_SALVADOR = "America/San_Salvador"
    AMERICA_PANAMA = "America/Panama"
    AMERICA_HAVANA = "America/Havana"
    
    # América sur y Caribe
    AMERICA_CARACAS = "America/Caracas"
    AMERICA_BOGOTA = "America/Bogota"
    AMERICA_LIMA = "America/Lima"
    AMERICA_QUITO = "America/Quito"
    AMERICA_LA_PAZ = "America/La_Paz"
    AMERICA_SANTIAGO = "America/Santiago"
    AMERICA_BUENOS_AIRES = "America/Argentina/Buenos_Aires"
    AMERICA_MONTEVIDEO = "America/Montevideo"
    AMERICA_ASUNCION = "America/Asuncion"
    AMERICA_SAO_PAULO = "America/Sao_Paulo"
    AMERICA_RIO_BRANCO = "America/Rio_Branco"
    AMERICA_CAYENNE = "America/Cayenne"
    AMERICA_PARAMARIBO = "America/Paramaribo"
    AMERICA_SANTO_DOMINGO = "America/Santo_Domingo"
    AMERICA_PUERTO_RICO = "America/Puerto_Rico"
    AMERICA_NASSAU = "America/Nassau"
    AMERICA_KINGSTON = "America/Kingston"
    AMERICA_PORT_AU_PRINCE = "America/Port-au-Prince"
    
    # Asia
    ASIA_TOKYO = "Asia/Tokyo"
    ASIA_SEOUL = "Asia/Seoul"
    ASIA_SHANGHAI = "Asia/Shanghai"
    ASIA_HONG_KONG = "Asia/Hong_Kong"
    ASIA_TAIPEI = "Asia/Taipei"
    ASIA_SINGAPORE = "Asia/Singapore"
    ASIA_KUALA_LUMPUR = "Asia/Kuala_Lumpur"
    ASIA_JAKARTA = "Asia/Jakarta"
    ASIA_BANGKOK = "Asia/Bangkok"
    ASIA_HO_CHI_MINH = "Asia/Ho_Chi_Minh"
    ASIA_YANGON = "Asia/Yangon"
    ASIA_DHAKA = "Asia/Dhaka"
    ASIA_KOLKATA = "Asia/Kolkata"
    ASIA_MUMBAI = "Asia/Mumbai"  # Sinónimo de Kolkata
    ASIA_KARACHI = "Asia/Karachi"
    ASIA_COLOMBO = "Asia/Colombo"
    ASIA_KATHMANDU = "Asia/Kathmandu"
    ASIA_DUBAI = "Asia/Dubai"
    ASIA_MUSCAT = "Asia/Muscat"
    ASIA_RIYADH = "Asia/Riyadh"
    ASIA_QATAR = "Asia/Qatar"
    ASIA_KUWAIT = "Asia/Kuwait"
    ASIA_BAHRAIN = "Asia/Bahrain"
    ASIA_BEIRUT = "Asia/Beirut"
    ASIA_JERUSALEM = "Asia/Jerusalem"
    ASIA_TEL_AVIV = "Asia/Tel_Aviv"
    ASIA_DAMASCUS = "Asia/Damascus"
    ASIA_AMMAN = "Asia/Amman"
    ASIA_BAGHDAD = "Asia/Baghdad"
    ASIA_TEHRAN = "Asia/Tehran"
    ASIA_KABUL = "Asia/Kabul"
    ASIA_TASHKENT = "Asia/Tashkent"
    ASIA_ALMATY = "Asia/Almaty"
    ASIA_NURSULTAN = "Asia/Nur-Sultan"
    ASIA_BISHKEK = "Asia/Bishkek"
    ASIA_DUSHANBE = "Asia/Dushanbe"
    ASIA_ASHGABAT = "Asia/Ashgabat"
    ASIA_YEREVAN = "Asia/Yerevan"
    ASIA_BAKU = "Asia/Baku"
    ASIA_TBILISI = "Asia/Tbilisi"
    
    # África
    AFRICA_CAIRO = "Africa/Cairo"
    AFRICA_CASABLANCA = "Africa/Casablanca"
    AFRICA_TUNIS = "Africa/Tunis"
    AFRICA_ALGIERS = "Africa/Algiers"
    AFRICA_TRIPOLI = "Africa/Tripoli"
    AFRICA_JOHANNESBURG = "Africa/Johannesburg"
    AFRICA_CAPE_TOWN = "Africa/Cape_Town"
    AFRICA_NAIROBI = "Africa/Nairobi"
    AFRICA_DAR_ES_SALAAM = "Africa/Dar_es_Salaam"
    AFRICA_KAMPALA = "Africa/Kampala"
    AFRICA_ADDIS_ABABA = "Africa/Addis_Ababa"
    AFRICA_LAGOS = "Africa/Lagos"
    AFRICA_ACCRA = "Africa/Accra"
    AFRICA_DAKAR = "Africa/Dakar"
    AFRICA_BAMAKO = "Africa/Bamako"
    AFRICA_OUAGADOUGOU = "Africa/Ouagadougou"
    AFRICA_LUANDA = "Africa/Luanda"
    AFRICA_WINDHOEK = "Africa/Windhoek"
    AFRICA_MAPUTO = "Africa/Maputo"
    AFRICA_HARARE = "Africa/Harare"
    AFRICA_LUSAKA = "Africa/Lusaka"
    AFRICA_KINSHASA = "Africa/Kinshasa"
    AFRICA_BRAZZAVille = "Africa/Brazzaville"
    AFRICA_DJIBOUTI = "Africa/Djibouti"
    AFRICA_MAURITIUS = "Africa/Mauritius"
    
    # Oceanía
    AUSTRALIA_SYDNEY = "Australia/Sydney"
    AUSTRALIA_MELBOURNE = "Australia/Melbourne"
    AUSTRALIA_BRISBANE = "Australia/Brisbane"
    AUSTRALIA_PERTH = "Australia/Perth"
    AUSTRALIA_ADELAIDE = "Australia/Adelaide"
    AUSTRALIA_DARWIN = "Australia/Darwin"
    AUSTRALIA_HOBART = "Australia/Hobart"
    AUSTRALIA_CANBERRA = "Australia/Canberra"
    PACIFIC_AUCKLAND = "Pacific/Auckland"
    PACIFIC_CHATHAM = "Pacific/Chatham"
    PACIFIC_FIJI = "Pacific/Fiji"
    PACIFIC_SAMOA = "Pacific/Samoa"
    PACIFIC_HONOLULU = "Pacific/Honolulu"
    PACIFIC_GUAM = "Pacific/Guam"
    PACIFIC_SAIPAN = "Pacific/Saipan"
    PACIFIC_PORT_MORESBY = "Pacific/Port_Moresby"
    PACIFIC_NOUMEA = "Pacific/Noumea"
    PACIFIC_SUVA = "Pacific/Suva"
    PACIFIC_TARAWA = "Pacific/Tarawa"
    PACIFIC_MAJURO = "Pacific/Majuro"
    PACIFIC_PAGO_PAGO = "Pacific/Pago_Pago"
    PACIFIC_RAROTONGA = "Pacific/Rarotonga"
    PACIFIC_TAHITI = "Pacific/Tahiti"
    PACIFIC_MARQUESAS = "Pacific/Marquesas"
    PACIFIC_GALAPAGOS = "Pacific/Galapagos"
    PACIFIC_EASTER = "Pacific/Easter"
    
    # Antártida
    ANTARCTICA_CASEY = "Antarctica/Casey"
    ANTARCTICA_DAVIS = "Antarctica/Davis"
    ANTARCTICA_DUMONTDURVILLE = "Antarctica/DumontDUrville"
    ANTARCTICA_MAWSON = "Antarctica/Mawson"
    ANTARCTICA_MCMURDO = "Antarctica/McMurdo"
    ANTARCTICA_PALMER = "Antarctica/Palmer"
    ANTARCTICA_ROTHERA = "Antarctica/Rothera"
    ANTARCTICA_SYOWA = "Antarctica/Syowa"
    ANTARCTICA_TROLL = "Antarctica/Troll"
    ANTARCTICA_VOSTOK = "Antarctica/Vostok"
    
    # Océano Índico
    INDIAN_MALDIVES = "Indian/Maldives"
    INDIAN_MAURITIUS = "Indian/Mauritius"
    INDIAN_COMORO = "Indian/Comoro"
    INDIAN_MAYOTTE = "Indian/Mayotte"
    INDIAN_REUNION = "Indian/Reunion"
    INDIAN_SEYCHELLES = "Indian/Seychelles"
    INDIAN_CHAGOS = "Indian/Chagos"
    INDIAN_COCOS = "Indian/Cocos"
    INDIAN_CHRISTMAS = "Indian/Christmas"
    
    # Zonas adicionales
    ATLANTIC_CANARY = "Atlantic/Canary"
    ATLANTIC_MADEIRA = "Atlantic/Madeira"
    ATLANTIC_AZORES = "Atlantic/Azores"
    ATLANTIC_CAPE_VERDE = "Atlantic/Cape_Verde"
    ATLANTIC_SOUTH_GEORGIA = "Atlantic/South_Georgia"
    ATLANTIC_STANLEY = "Atlantic/Stanley"
    ATLANTIC_BERMUDA = "Atlantic/Bermuda"
    ATLANTIC_FAEROE = "Atlantic/Faroe"
    ATLANTIC_ICELAND = "Atlantic/Reykjavik"
    
    @classmethod
    def get_zone(cls, name: str) -> Optional['Timezone']:
        """Obtener zona horaria por nombre"""
        try:
            return cls[name]
        except KeyError:
            return None
    
    @classmethod
    def list_all(cls) -> List[str]:
        """Listar todas las zonas horarias disponibles"""
        return [zone.value for zone in cls]
    
    @classmethod
    def list_by_continent(cls, continent: str) -> List[str]:
        """Listar zonas por continente (EUROPE, AMERICA, ASIA, AFRICA, AUSTRALIA, PACIFIC)"""
        prefix = continent.upper()
        return [zone.value for zone in cls if zone.name.startswith(prefix)]
    
    @classmethod
    def get_timezone(cls, zone_name: str) -> Optional['Timezone']:
        """Obtener enumerador desde string"""
        try:
            return cls(zone_name)
        except ValueError:
            return None
    
    @property
    def pytz_zone(self):
        """Retorna la zona para usar con pytz"""
        return self.value
    
    def __str__(self):
        return self.value
