"""
Funktioner till main-programmmet
"""
from operator import itemgetter
import time

filename_e = "easy.txt"
filename_m = "medium.txt"
filename_h = "hard.txt"
filename_s = "score.txt"

def clear_screen():
    """
    "Rensar" skärmen, bättre upplevelse för användaren
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")


def read_file_e():
    """
    returnerar raderna i filen easy.txt som en lista
    """
    with open(filename_e) as fh:
        content_e_list = fh.readlines()
        return content_e_list


def read_file_m():
    """
    returnerar raderna i filen medium.txt som en lista
    """
    with open(filename_m) as fh:
        content_m_list = fh.readlines()
        return content_m_list


def read_file_h():
    """
    returnerar raderna i filen hard.txt som en lista
    """
    with open(filename_h) as fh:
        content_h_list = fh.readlines()
        return content_h_list


def len_read_file_e():
    """
    returnerar antal tecken i easy.txt
    """
    content_e_list = read_file_e()
    strip_e_list = [i.strip() for i in content_e_list]
    content = "".join(strip_e_list)
    length = len(content)
    return length


def len_read_file_m():
    """
    returnerar antal tecken i medium.txt
    """
    content_m_list = read_file_m()
    strip_m_list = [i.strip() for i in content_m_list]
    content = "".join(strip_m_list)
    length = len(content)
    return length


def len_read_file_h():
    """
    returnerar antal tecken i hard.txt
    """
    content_h_list = read_file_h()
    strip_h_list = [i.strip() for i in content_h_list]
    content = "".join(strip_h_list)
    length = len(content)
    return length


def easy():
    """
    stripar den hämtade listan från funktionen,
    loopar genom den genom att skriva ut en rad i taget
    där användaren ska skriva av, skickar användarens sträng till uträkningsfunktionen
    """
    content_e_list = read_file_e()
    strip_e_list = [i.strip() for i in content_e_list]

    result = ""
    start_time = time.time()
    for i in strip_e_list:
        clear_screen()
        print(i)
        result += input("")
    end_time = time.time()

    content = "".join(strip_e_list)
    length = len_read_file_e()

    calc_result(content, result, length, start_time, end_time)


def medium():
    """
    stripar den hämtade listan från funktionen,
    loopar genom den genom att skriva ut en rad i taget
    där användaren ska skriva av, skickar användarens sträng till uträkningsfunktionen
    """
    content_m_list = read_file_m()
    strip_m_list = [i.strip() for i in content_m_list]

    result = ""
    start_time = time.time()
    for i in strip_m_list:
        clear_screen()
        print(i)
        result += input("")
    end_time = time.time()

    content = "".join(strip_m_list)
    length = len_read_file_m()

    calc_result(content, result, length, start_time, end_time)


def hard():
    """
    stripar den hämtade listan från funktionen,
    loopar genom den genom att skriva ut en rad i taget
    där användaren ska skriva av, skickar användarens sträng till uträkningsfunktionen
    """
    content_h_list = read_file_h()
    strip_h_list = [i.strip() for i in content_h_list]

    result = ""
    start_time = time.time()
    for i in strip_h_list:
        clear_screen()
        print(i)
        result += input("")
    end_time = time.time()

    content = "".join(strip_h_list)
    length = len_read_file_h()

    calc_result(content, result, length, start_time, end_time)


def calc_result(content, result, length, start_time, end_time):
    """
    Tar emot data från vår användare, loopar genom vilka tecken som blivit fel,
    skriver ut feltecken, fel% och räknar ut vilken poäng användaren fått, 
    slutligen skrivs resultatet tillsammans med användarens namn in till filen score.txt
    """

    dict_errors = {}
    index = 0
    error_counter = 0

    for letter in content:
        try:
            if letter == result[index]:
                index += 1
            else:
                if letter not in dict_errors:
                    dict_errors[letter] = 1
                    index += 1
                    error_counter += 1
                else:
                    dict_errors[letter] += 1
                    index += 1
                    error_counter += 1
        except IndexError:
            if letter not in dict_errors:
                dict_errors[letter] = 1
                index += 1
                error_counter += 1
            else:
                dict_errors[letter] += 1
                index += 1
                error_counter += 1

    clear_screen()
    input("Press enter to see result...")
    clear_screen()

    duration = int(end_time - start_time)
    len_result = len(result)
    cpm = int((len_result/duration) * 60)
    sorted_dict_errors = sorted(dict_errors.items(), key=itemgetter(1), reverse=True)
    error_percentage = int((error_counter / length) * 100)
    points = int((length * (100 - error_percentage)) / duration)
    msg = (f"Feltecken:\n{sorted_dict_errors}\nFelprocent: {error_percentage}%\nCPM: {cpm}\nPoäng: {points}")
    print(msg)
    name = input("Enter username to add score: ")
    name = name.replace(" ", "") 

    name_points = (f"\n-{name} {points}")

    with open(filename_s, "a") as fh:
        fh.write(name_points)


def read_file_s():
    """
    läser in raderna i filen score.txt som en lista,
    sorterar listan via ett dictionary, skriver ut namn + poäng 
    i fallande storleksordning sorterat på poäng
    """
    clear_screen()
    with open(filename_s) as fh:
        content_s_list = fh.readlines()
        strip_s_list = [i.strip() for i in content_s_list]

        name_list = []
        point_list = []
        for i in strip_s_list[1:]:
            name_list.append(i.split()[0])
            point_list.append(i.split()[1])

        dict_result = {}
        for index, i in enumerate(name_list):
            dict_result[i] = int(point_list[index])

        sorted_dict_result = sorted(dict_result.items(), key=itemgetter(1), reverse=True)
        for key, value in sorted_dict_result:
            print(key, value)
