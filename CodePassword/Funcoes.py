dicionario = {
    'A' : 'q',
    'B' : 'w',
    'C' : 'e',
    'D' : 'r',
    'E' : 't',
    'F' : 'y',
    'G' : 'u',
    'H' : 'i',
    'I' : 'o',
    'J' : 'p',
    'K' : 'a',
    'L' : 's',
    'M' : 'd',
    'N' : 'f',
    'O' : 'g',
    'P' : 'h',
    'Q' : 'j',
    'R' : 'k',
    'S' : 'l',
    'T' : 'z',
    'U' : 'x',
    'V' : 'c',
    'X' : 'v',
    'Y' : 'b',
    'Z' : 'n',
    'Ç' : 'm',
    'a' : 'Q',
    'b' : 'W',
    'c' : 'E',
    'd' : 'R',
    'e' : 'T',
    'f' : 'Y',
    'g' : 'U',
    'h' : 'I',
    'i' : 'O',
    'j' : 'P',
    'k' : 'A',
    'l' : 'S',
    'm' : 'D',
    'n' : 'F',
    'o' : 'G',
    'p' : 'H',
    'q' : 'J',
    'r' : 'K',
    's' : 'L',
    't' : 'Z',
    'u' : 'X',
    'v' : 'C',
    'x' : 'V',
    'y' : 'B',
    'z' : 'N',
    'ç' : 'M',
    '!' : '+',
    '@' : '-',
    '#' : ')',
    '$' : '(',
    '%' : '*',
    '¨' : '&',
    '&' : '!',
    '*' : '@',
    '(' : '#',
    ')' : '$',
    '-' : '%',
    '+' : '¨',
    '=' : '_',
    '_' : '?',
    '.' : '(',
    '>' : '<',
    ':' : ';',
    ';' : ':',
    "'" : "|",
    '0' : '9',
    '1' : '8',
    '2' : '7',
    '3' : '6',
    '4' : '5',
    '5' : '4',
    '6' : '3',
    '7' : '2',
    '8' : '1',
    '9' : '0',
    ' ' : '¬'
}

def codificar (senha):
    codificado = []
    for i in range (len(senha)):
        codificado.insert(i, (dicionario[senha[i]]))
    codificado.reverse()
    codificado.insert(1, codificado[len(codificado)-2])
    codificado.pop(len(codificado)-2)
    return "".join(codificado)

def descodificar (codificada):
    codigo = list(codificada)

    codigo.insert((len(codigo)-1), codigo[1]) 
    codigo.pop(1)
    codigo.reverse()
    chaves = list(dicionario.keys())
    valores = list(dicionario.values())
    senha = []
    for i in range(len(codigo)):
        posicao = valores.index(codigo[i])
        senha.insert(i, chaves[posicao])
    return "".join(senha)