
Fraza = "Я йшов вулицею почала звучати тривога тривога тривога тривога, вулиця була незнайома. /" \
        "Я не знав де бомбосховище. Хто я. Через тривогу в мене з'явилась внутрішня / " \
        "тривога. Хто я. Я не знаю як записати 'тривогу' в тривога. Потрібна регулярка /" \
        "або записати через 'і' в кондішенах-умовах "

Fraza_list = Fraza.split()

Fraza_result = [ i * len(word) for word in Fraza_list if word == "тривога" for i in range(17)]
counter = 0




# for i in range(len(Fraza_list)):
#     if Fraza_list[i] == "тривога" or Fraza_list[i] == "тривогу":
#         counter += 1
#         Fraza_result.append(i)


print("Counter = ", counter)
print("Fraza_result", Fraza_result)
print("Fraza_list = ", Fraza_list)