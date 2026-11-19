from pyscript import window, display
from urllib.parse import parse_qs

parametros = parse_qs(window.location.search.lstrip("?"))

if "numero1" in parametros and "numero2" in parametros:
    n1 = float(parametros["numero1"][0])
    n2 = float(parametros["numero2"][0])
    display(f" {n1 + n2}", target="resultado")
