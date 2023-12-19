def obter_periodo():
    print()
    print('Digite o período:')
    print('digite [1] para anos')
    print('digite [2] para meses')
    print()
    periodo = input('Digite: ')
    
    if periodo == '1':
        anos = int(input('Anos: '))
        return anos * 12
    elif periodo == '2':
        return int(input('pmt: '))
    else:
        return 0

def calcular_rentabilidade(capital_inicial, periodo, taxa_juros):
    total = []
    lista = []
    
    for _ in range(periodo):
        s1 = sum(lista)
        
        if s1 < 1:
            lista.append(1)
            s1 = sum(lista)
            t1 = capital_inicial * taxa_juros
            total.append(t1)
        else:
            lista.append(1)
            s2 = sum(lista)
            total.append(capital_inicial)
            t2 = sum(total)
            s3 = t2 * taxa_juros
            t2 = s3
            total = []
            total.append(s3)
    
    return total, s2

if __name__ == '__main__':
    print('')
    print('')
    print('')
    capital_inicial = float(input('Capital inicial/Aporte: ').replace(',', '.'))
    periodo = obter_periodo()
    taxa_juros = float(input('Taxa de juros: ').replace(',', '.'))
    
    resultados, total_aportes = calcular_rentabilidade(capital_inicial, periodo, 1 + (taxa_juros / 100))
    
    print('----------------------------------')
    print(f'Aportes mensais R$ {capital_inicial}')
    print(f'Total investido R$ {capital_inicial * periodo}')
    print(f'Taxa de juros mensal: {taxa_juros}%')
    print(f'Capitalizado R$ {resultados[-1] - (capital_inicial * periodo)}')
    print(f'Total do capital R$ {resultados[-1]}')
    print('----------------------------------')
    print(f'Rendimento mensal: R$ {(resultados[-1] * (1 + (taxa_juros / 100))) - resultados[-1]}')
