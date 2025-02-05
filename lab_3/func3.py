def sana(basss, ayaq):
    for tauyqtar in range(basss + 1):
        qoiyan = basss - tauyqtar
        if 2 * tauyqtar + 4 * qoiyan == ayaq:
            return tauyqtar, qoiyan
    return None

print(sana(12,34))
