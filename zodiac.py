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
    nakshatra = math.floor(xx[0] / (360 / 27))  # There are 27 nakshatras, each spanning 360/27 degrees
    nakshatras = [
        'Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra', 'Punarvasu', 'Pushya', 'Ashlesha',
        'Magha', 'Purva Phalguni', 'Uttara Phalguni', 'Hasta', 'Chitra', 'Swati', 'Vishakha', 'Anuradha',
        'Jyeshtha', 'Mula', 'Purva Ashadha', 'Uttara Ashadha', 'Shravana', 'Dhanishtha', 'Shatabhisha',
        'Purva Bhadrapada', 'Uttara Bhadrapada', 'Revati'
    ]
    nakshatras_in_tamil = ['அசுவினி', 'பரணி', 'கிருத்திகை', 'ரோகிணி', 'மிருகசிரீஷம்', 'திருவாதிரை', 'புனர்பூசம்', 'பூசம்', 'ஆயில்யம்', 'மகம்', 'பூரம்', 'உத்திரம்', 'ஹஸ்தம்', 'சித்திரை', 'சுவாதி', 'விசாகம்', 'அனுஷம்', 'கேட்டை', 'மூலம்', 'பூராடம்', 'உத்திராடம்', 'திருவோணம்', 'அவிட்டம்', 'சதயம்', 'பூரட்டாதி', 'உத்திரட்டாதி', 'ரேவதி']
    # return nakshatras[nakshatra]
    return f'{nakshatras_in_tamil[nakshatra]} / {nakshatras[nakshatra]}'


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
dt= "12/02/98 06:52:45"
dt = datetime.datetime.strptime(dt, '%d/%m/%y %H:%M:%S')
print(check_raasi(dt))
print(check_nakshatra(dt))

