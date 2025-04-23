import re
import main_functions as m_f


our_dict = m_f.create_dict('haiku.txt')
pattern = re.compile(r'[АЕЁИОУЫЭЮЯаеёиоуыэюя]')
m_f.check_haiku(our_dict, pattern)


