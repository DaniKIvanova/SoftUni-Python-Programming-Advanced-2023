def symbol_occurrences(data):
    symbol_occur = {}
    for symbol in data:
        if symbol not in symbol_occur:
            symbol_occur[symbol] = 1
        else:
            symbol_occur[symbol] += 1
    return symbol_occur


def print_result(symbol_occur):
    for symbol, occur in sorted(symbol_occur.items()):
        print(f"{symbol}: {occur} time/s")


symbols = tuple(map(str, input()))
symbols_count = symbol_occurrences(symbols)
print_result(symbols_count)

