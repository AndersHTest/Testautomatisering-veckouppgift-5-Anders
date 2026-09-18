def temperaturomvandling(enhet, temp):

    fahrenheit = ["f", "F"]
    celsius = ["c", "C"]

    if enhet in fahrenheit:
        temp_c = (temp - 32) * 5 / 9
        return temp_c

    elif enhet in celsius:
        temp_f = (temp * 1.8) + 32
        return temp_f

    else:
        return None
