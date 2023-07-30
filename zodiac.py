import datetime
import math
import swisseph as swe

def check_nakshatra(dt):
    month, day, year = dt.month, dt.day, dt.year
    hour, minute = dt.hour, dt.minute
    ut = hour + (minute / 60)
    jd = swe.julday(year, month, day, ut)

    # Calculate the Moon's position in the sidereal zodiac
    flags = swe.FLG_SWIEPH | swe.FLG_SIDEREAL
    swe.set_sid_mode(swe.SIDM_LAHIRI)  # Use the Lahiri ayanamsa for sidereal calculations
    xx, ret = swe.calc_ut(jd, swe.MOON, flags)

    # Calculate the nakshatra based on the Moon's position
    nakshatra = (xx[0] / (360 / 27))  # There are 27 nakshatras, each spanning 360/27 degrees
    # print(nakshatra)
    nakshatra = math.floor(nakshatra)
    nakshatra = nakshatra % 27
    nakshatras = [
        'Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra', 'Punarvasu', 'Pushya', 'Ashlesha',
        'Magha', 'Purva Phalguni', 'Uttara Phalguni', 'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha',
        'Jyeshtha', 'Mula', 'Purva Ashadha', 'Uttara Ashadha', 'Shravana', 'Dhanishtha', 'Shatabhisha',
        'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati'
    ]
    nakshatras_in_tamil = ['அசுவினி', 'பரணி', 'கிருத்திகை', 'ரோகிணி', 'மிருகசிரீஷம்', 'திருவாதிரை', 'புனர்பூசம்', 'பூசம்', 'ஆயில்யம்', 'மகம்', 'பூரம்', 'உத்திரம்', 'ஹஸ்தம்', 'சித்திரை', 'சுவாதி', 'விசாகம்', 'அனுஷம்', 'கேட்டை', 'மூலம்', 'பூராடம்', 'உத்திராடம்', 'திருவோணம்', 'அவிட்டம்', 'சதயம்', 'பூரட்டாதி', 'உத்திரட்டாதி', 'ரேவதி']

    pada_degrees = 360 / 108  # Each nakshatra is divided into 4 padas, each spanning 360/108 degrees
    nakshatra_pada = math.floor(xx[0] / pada_degrees/4)
    nakshatra_pada = nakshatra_pada % 4
    # error by 1 pada
    # b
    nakshatra_padas = ['1st pada', '2nd pada', '3rd pada', '4th pada']
    nakshatra_padas_in_tamil = ['1வது பாதம்', '2வது பாதம்', '3வது பாதம்', '4வது பாதம்']
    
    # return f'{nakshatras[nakshatra]} - {nakshatra_padas[nakshatra_pada]} / {nakshatras_in_tamil[nakshatra]} - {nakshatra_padas_in_tamil[nakshatra_pada]}'
    np = nakshatra_pada + 1
    return f'{nakshatras_in_tamil[nakshatra]} - {np} / {nakshatras[nakshatra]} - {np}'


def check_raasi(dt):
    month, day, year = dt.month, dt.day, dt.year
    hour, minute = dt.hour, dt.minute
    ut = hour + (minute / 60)
    jd = swe.julday(year, month, day, ut)

    # Calculate the Moon's position in the sidereal zodiac
    flags = swe.FLG_SWIEPH | swe.FLG_SIDEREAL
    swe.set_sid_mode(swe.SIDM_LAHIRI)  # Use the Lahiri ayanamsa for sidereal calculations
    xx, ret = swe.calc_ut(jd, swe.MOON, flags)

    # Calculate the raasi based on the Moon's position
    raasi = math.floor(xx[0] / (360 / 12))  # There are 12 raasis, each spanning 360/12 degrees
    raasi = raasi % 12
    
    raasis = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius',
        'Capricorn', 'Aquarius', 'Pisces'
    ]
    raasis_in_tamil = [
        'மேஷம்', 'ரிஷிபம்', 'மிதுனம்', 'கடகம்', 'சிம்மம்', 'கன்னி', 'துலாம்', 'விருச்சிகம்', 'தனுசு',
        'மகரம்', 'கும்பம்', 'மீனம்'
    ]

    return f'{raasis_in_tamil[raasi]} / {raasis[raasi]}'



# Example usage:

if __name__ == '__main__':
    from pyperclip import paste
    dt = paste()
    dt = '12/02/1998 06:52:45'
    dt = '8/12/2000 10:55:00'
    try:
        dt = datetime.datetime.strptime(dt, '%d/%m/%y %H:%M:%S')
    except:
        dt = datetime.datetime.strptime(dt, '%d/%m/%Y %H:%M:%S')
    print(dt)
    raasi=(check_raasi(dt))
    nakshatra=(check_nakshatra(dt))
    msg = f"இராசி : {raasi}\nநட்சத்திரம் : {nakshatra}"
    from pyperclip import copy
    copy(msg)
    print(msg)