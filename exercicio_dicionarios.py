perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1','2','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5+5?',
        'Opções': ['5','9','6','8','10'],
        'Resposta': '10',
    },
    {
        'Pergunta': 'Quanto é 2*3?',
        'Opções': ['6','2','3','4','5'],
        'Resposta': '6',
    },
]

for i in range(0, 3):
    pergunta = perguntas[i]["Pergunta"]
    opcao = perguntas[i]["Opções"]
    print("Pergunta: ",pergunta)
    print("Opções:")
    print(opcao)
