def CakeCandles():

        candles = [3, 2, 1, 3]
        countCandle = 0
        Candle = max(candles)

        for i in candles:
            if i == Candle:
                countCandle += 1

        print(countCandle)

CakeCandles()