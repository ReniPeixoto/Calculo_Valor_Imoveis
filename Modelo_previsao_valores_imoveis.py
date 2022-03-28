''' Projeto de Data Science para previsão de valores de Imóveis de acordo com tamanho.

Lista 1: Preços Reais dos Imóveis
Lista 2: Tamanho do imóvel.'''


precos_imoveis = [328383.93, 233046.66, 219427.05, 293578.26, 358649.73, 348056.70, 270878.91, 272392.20, 340490.25,
                  207320.73, 363189.60, 260285.88, 302658.00, 255746.01, 246666.27, 304171.29, 340490.25, 243639.69,
                  154355.58, 180081.51, 281471.94, 325357.35, 307197.87, 243639.69, 230020.08, 236073.24, 255746.01,
                  222453.63, 164948.61, 373782.63, 245152.98, 325357.35, 273905.49, 376809.21, 314764.32, 154355.58,
                  254232.72, 231533.37, 181594.80, 195214.41, 284498.52, 290551.68, 323844.06, 295091.55, 375295.92,
                  369242.76, 213373.89, 299631.42, 286011.81, 255746.01, 295091.55, 214887.18, 237586.53, 351083.28,
                  186134.67, 216400.47, 204294.15, 225480.21, 361676.31, 358649.73, 196727.70, 340490.25, 226993.50,
                  204294.15, 311737.74, 158895.45, 257259.30, 346543.41, 369242.76, 316277.61, 273905.49, 308711.16,
                  370756.05, 214887.18, 316277.61, 331410.51, 316277.61, 151329.00, 337463.67, 210347.31, 302658.00,
                  195214.41, 234559.95, 252719.43, 311737.74, 286011.81, 313251.03, 361676.31, 292064.97, 228506.79,
                  261799.17, 251206.14, 178568.22, 171001.77, 255746.01, 375295.92, 190674.54, 264825.75, 228506.79,
                  261799.17]

tamanho_imoveis = [207, 148, 130, 203, 257, 228, 160, 194, 232, 147, 222, 165, 184, 175, 147, 217, 214, 171, 86, 111,
                   180, 211, 210, 168, 156, 154, 179, 163, 99, 246, 162, 205, 195, 263, 198, 121, 149, 140, 122, 119,
                   197, 210, 218, 202, 258, 256, 135, 203, 173, 152, 197, 145, 154, 252, 141, 141, 151, 133, 232, 229,
                   134, 215, 155, 138, 186, 120, 152, 213, 256, 219, 200, 210, 238, 140, 224, 233, 222, 120, 233, 151,
                   185, 111, 149, 186, 194, 194, 222, 223, 185, 157, 154, 164, 129, 128, 169, 240, 136, 191, 157, 154]


def valor_justo(precos=precos_imoveis, tamanho=tamanho_imoveis, fator=0.1):
    if len(precos) != len(tamanho):
        print('As listas com os preços e tamanhos dos imoveis não tem a mesma quantidades de itens')
        return None
    else:
        indice = int((1 - fator) * len(precos))
        precos_treino = precos[:indice]
        precos_teste = precos[indice:]
        tamanho_treino = tamanho[:indice]
        tamanho_teste = tamanho[indice:]
        print(f'O teste e o treino será efetuado com uma amostragem de {len(precos)} Imóveis')
        print('-' * 70)

        m2_treino = sum(precos_treino) / sum(tamanho_treino)
        m2_teste = sum(precos_teste) / sum(tamanho_teste)
        print(f'No modo TREINO o sistema calculou o valor de R$ {m2_treino:_.2f} por M² do imóvel'.replace('.',',').replace('_','.'))
        print(f'No mode TESTE o sistema calculou o valor de R$ {m2_teste:_.2f} por M² do imóvel '.replace('.',',').replace('_','.'))
        print(f'Entre as duas verificações houve uma diferença de {m2_teste * 100 / m2_treino - 100:.2f}%')
        print('-' * 70)
        imovel = input('Digite o tamanho do imóvel em m² para estimar o valor: ').strip().replace(',', '.')
        imovel = float(imovel)
        print(f'Valor do imóvel estimado em R$ {imovel * m2_teste:_.2f}'.replace('.',',').replace('_','.'))

valor_justo()
