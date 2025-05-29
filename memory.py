# memory.py

# Basit bir "bellek" olarak liste kullanalım
bellek = []

def yaz_bellege(veri):
    bellek.append(veri)

def oku_bellekten(index):
    if index < 0 or index >= len(bellek):
        return None
    return bellek[index]

def bellegi_goster():
    return list(enumerate(bellek))
