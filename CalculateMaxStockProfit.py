from operator import itemgetter

class StockMaxProfit():

    def maxProfit(priceindex):
        temp_index = {}
        result_list = []

        for buytime, buyprice in priceindex.items():

            profit_list = []
            final_list = []

            temp_index[buytime] = buyprice

            for selltime in priceindex:
                if selltime not in temp_index.keys():
                    sellprice = priceindex[selltime]
                    profit = sellprice - buyprice
                    profit_list.append({"Buytime":buytime, "Buyprice":buyprice, "Selltime":selltime, "Sellprice":sellprice, "MaxProfit":round(profit, 1)})

            out = max(profit_list, key=itemgetter("MaxProfit"), default=0)
            final_list.append(out)
            result_list.append(final_list[0])

            endresult = result_list[:-1]
        highestprofit = list((max(endresult, key=itemgetter("MaxProfit"), default=0)).values())[4]

        for stockresult in list(endresult):

            for key,value in stockresult.items():
                if value == highestprofit:
                    for key in stockresult:
                        print(key, '=', stockresult[key])
                    print('----------------')


if __name__ == '__main__':
    Priceindex = {"9:00": 1.2, "9:30": 1.3, "10:00": 1.4, "10:30": 1.5, "11:00": 1.6, "11:30": 1.4, "12:00": 1.2,
                    "12:30": 1.0, "13:00": 0.8, "13:30": 0.9, "14:00": 1.1, "14:30": 1.3, "15:00": 1.4, "15:30": 1.2,
                    "16:00": 1.1, "16:30": 0.7, "17:00": 1.3}

    StockMaxProfit.maxProfit(priceindex = Priceindex)


















