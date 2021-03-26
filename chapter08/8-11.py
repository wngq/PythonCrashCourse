magicians = ['david copperfield', 'derren brown', 'michael ammar']


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


def make_great(m_list):
    length_m_list = len(m_list)
    for m_index in range(0, length_m_list):
        m_list[m_index] = "The Great " + m_list[m_index]

    return m_list


changed_magicians = make_great(magicians[:])
show_magicians(changed_magicians)

show_magicians(magicians)
