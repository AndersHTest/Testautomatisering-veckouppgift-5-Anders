def temperaturomvandling(enhet, temp):

    fahrenheit = ["f", "F"]
    celsius = ["c", "C"]

    if enhet in fahrenheit:
        temp_c = (temp - 32) * 5 / 9
        return f"{temp} grader Fahrenheit blir {round(temp_c, 1)} grader Celsius."

    elif enhet in celsius:
        temp_f = (temp * 1.8) + 32
        return f"{temp} grader Celsius blir {round(temp_f, 1)} grader Fahrenheit."

    else:
        return None
