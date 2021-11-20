# Zadanie 26
import re

txt = "To be, or not to be, that is the question"
reg = "\w+"

answear = re.findall(reg, txt)
print(f"Liczba słów: {len(answear)}")
