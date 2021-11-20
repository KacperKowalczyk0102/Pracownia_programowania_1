# Zadanie 25
import re

txt = "To be, or not to be, that is the question"
reg = "[aeiouyąęó]"

answear = re.findall(reg, txt)
print(f"Liczba samogłosek: {len(answear)}")

