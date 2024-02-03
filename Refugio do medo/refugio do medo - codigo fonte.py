import random


def salvar_jogo(ponto_do_jogo: str, nome: str):
    with open("progresso.txt", "w") as arquivo:
        arquivo.write(f"{ponto_do_jogo}|{nome}")


def carregar_jogo():
    try:
        with open("progresso.txt", "r") as arquivo:
            data = arquivo.read().strip().split("|")
            if len(data) == 2:
                return data[0], data[1]
            else:
                return data[0], ""
    except FileNotFoundError:
        return None


def menu():
    print(
        "--------------------------------------------------------------------------------------------------------"
    )
    print("Seja bem-vindo(a) ao Refúgio do medo. Espero que se divirta. :)")
    print("1. Jogar")
    print("2. Como jogar")
    print("3. Sair")


def verificar_progresso_salvo():
    progresso, nome = carregar_jogo()
    if progresso:
        print("Jogo salvo encontrado!")
        user_input = input(
            "Deseja começar um novo jogo ou continuar o último jogo salvo? (1. Novo jogo, 2. Continuar): "
        )
        if user_input == "1":
            return "novo_jogo", ""
        elif user_input == "2":
            return progresso, nome
        else:
            print("Opção inválida.")
            return None, ""
    else:
        return "novo_jogo", ""


def jogar(progresso, nome_coelho=""):
    if progresso == "novo_jogo":
        nome_coelho = input("Antes de começar, digite o seu apelido: ")
        inicio(nome_coelho)
    elif progresso == "inicio_do_jogo":
        print()
        inicio(nome_coelho)
    elif progresso == "escolha_pernoite":
        print("Continuando do ponto salvo...")
        print()
        pernoite(nome_coelho)
    elif progresso == "explorar_casa":
        print("Continuando do ponto salvo...")
        print()
        explorar_casa(nome_coelho)
    elif progresso == "jantar_em_andamento":
        print("Continuando do ponto salvo...")
        print()
        jantar(nome_coelho)
    else:
        print("Progresso desconhecido.")


def como_jogar():
    print(
        "--------------------------------------------------------------------------------------------------------"
    )
    print(
        "DICAS:\n\
Suas escolhas são extremamentes importantes para o caminhar do jogo e TODAS ELAS tem consequencias.\n\
As respostas terão uma espécie de sinalizador de segurança\n\
VERDE: seguro, AMARELO: cuidado, VERMELHO: voce se fodeu.\n\
O senhor Lobo sempre vai esperar o melhor de voce, então... seja gentil.\n\
O senhor lobo não gosta de barulhos muito altos.\n\
Não toque e nem faça nada sem a permissão do anfitrião, voce não está na sua casa.\n\
Em hipotese alguma entre no escritório do Senhor Lobo, ele ODEIA pessoas incheridas.\n\
Não saia do seu quarto no meio da noite, para sua própria segurança.\n"
    )
    user_input = input("Pressione Enter para voltar ao menu principal.")


def inicio(nome_coelho):
    escolha_inicio = {
        "1": "bater_na_porta",
        "2": "ignorar_e_ir_embora",
        "3": "salvar_e_voltar_ao_menu",
    }
    print(
        "\n-------------------------------------------------------------------------------------------------------------------------------------------------------------"
    )
    print(
        f"{nome_coelho} é um pequeno coelho correndo pelo bosque em uma noite chuvosa... Suas roupas estão enxarcadas, ele esta cansado e procura por abrigo.\n\
Sua vista está completamente embassada por causa da água que escorre dos pelos das suas orelhas até seus olhos. Mas, em um certo ponto, relampagos\n\
começaram a iluminar seu caminho e, de longe, o pequeno coelho avista no meio do bosque um campo aberto com um chalé situado bem em seu centro. Rapidamente\n\
{nome_coelho} pensa que aquele chalé seria um ótimo abrigo contra a chuva então continua correndo até ele. Ao se aproximar ele nota luzes acessas, fumaça\n\
saindo pela chaminé e um clima bastante agradável comparado ao inferno em que se encontrara por culpa da chuva."
    )

    print()
    print(
        "1. Bater na porta do chalé\n"
        "2. Ignorar e ir embora\n"
        "3. Salvar e voltar ao menu inicial\n"
    )

    escolha = input(f"O que {nome_coelho} escolhe fazer? ")

    if escolha in escolha_inicio:
        if escolha_inicio[escolha] == "bater_na_porta":
            print(
                f"\nEntão, {nome_coelho} decide dar 3 batidas na\n\
porta e rezar para ser atendido(a) por uma doce senhora fazendo biscoitos de leite ninho com nutella (iguais os que sua mãe fazia na primavera) mas\n\
é surpreendido por um lobo alto em vestimentas dignas de um baile de gala. Ele vestia um terno preto, calça de alfaiataria e um belo par de sapatos.\n\
Ele tinha um olhar sério e indecifravel. Voce estava morrendo de medo mas tentou ao máximo esconder enquanto ele o analisava de cabo a rabo.\n\
\n      LOBO: Ora, entre, entre! Voce está completamente molhado, irei lhe ajudar. - disse o lobo mudando sua expressão e falando em um tom preocupado.\n\
\n{nome_coelho} entra sem pensar duas vezes, pega a toalha que o Lobo deu a voce e se seca enquanto ele o observa.\n\
\n      LOBO:Pequeno coelho, qual é o seu nome? - pergunta o lobo.\n\
        COELHO: Meu nome é {nome_coelho}, e o seu?\n\
        SENHOR LOBO: Pode me chamar de Senhor Lobo. Então... {nome_coelho}, faz bastante tempo desde que eu recebi uma visita. Voce gostaria de se juntar a mim para o jantar?"
            )
            print()
            jantar(nome_coelho)
        elif escolha_inicio[escolha] == "ignorar_e_ir_embora":
            print(
                "O coelho acha suspeito um lindo chalé daqueles no meio da floresta e então prefere buscar abrigo em outro lugar.\n\
\nFIM\n"
            )
        elif escolha_inicio[escolha] == "salvar_e_voltar_ao_menu":
            salvar_jogo("inicio_do_jogo", nome_coelho)
            print("Jogo salvo com sucesso! Voltando ao menu inicial.")
            return
        else:
            print("Opção inválida.")


def receita_aleatoria():
    receitas = [
        (
            "Sopa de Legumes",
            [
                "Pique os legumes em pequenos pedaços",
                "adicione em uma panela grande 2 litros de água junto aos legumes",
                "cozinhe em fogo baixo por 1 hora.",
            ],
        ),
        (
            "Risoto de cogumelos",
            [
                "Refogue alho, cebola e os cogumelos em uma frigideira",
                "adicione arroz e vinho branco",
                "cozinhe até ficar cremoso.",
            ],
        ),
        (
            "PF do Mestre dos Magos (UFRJ)",
            ["Adicione tudo o que tem direito e seja feliz, não tem como dar errado."],
        ),
        (
            "Frango assado",
            [
                "Tempere o frango com páprica, sal e pimenta",
                "asse por 2 horas a 180 graus.",
            ],
        ),
    ]

    receita_escolhida, passos = random.choice(receitas)
    return receita_escolhida, passos


def jantar(nome_coelho):
    escolhas_jantar = {"1": "aceitar", "2": "recusar", "3": "salvar_e_voltar_ao_menu"}

    print(
        "1. Aceitar o convite e jantar com o Senhor Lobo.\n"
        "2. Recusar o convite e dizer que não está com fome.\n"
        "3. Salvar e voltar ao menu inicial.\n"
    )
    escolha = input(f"O que {nome_coelho} deseja fazer? ")
    print()

    if escolha in escolhas_jantar:
        print(
            "--------------------------------------------------------------------------------------------------------"
        )
        if escolhas_jantar[escolha] == "aceitar":
            print(f"{nome_coelho} aceitou jantar com o Senhor Lobo.")
            print()
            print(
                f"O Senhor Lobo ficou feliz com a escolha de {nome_coelho}, ele está animado com a sua visita! (VERDE)\n\
Para ser educado(a) {nome_coelho} se ofereceu para cozinhar para o Senhor Lobo, até porque, {nome_coelho} iria comer e beber de graça naquela noite\n\
e queria fazer algo para ajudar com essas despesas. O Senhor Lobo aceitou o pedido do pequeno coelho e lhe entregou um livro de receitas para que\n\
{nome_coelho} pudesse preparar a receita do seu gosto.\n"
            )

            receita_nome, receita_escolhida = receita_aleatoria()

            print(
                f"{nome_coelho} abre o livro de receitas e escolhe a receita: {receita_nome}, instruções: {receita_escolhida}\n\
O coelho então começa a preparar o jantar, seguindo cuidadosamente as instruções do livro enquanto o Senhor Lobo o observava atentamente.\n\
Depois de concluir e montar com perfeição os pratos com um delicioso {receita_nome}, {nome_coelho} serviu um jantar maravilhoso que fizeram\n\
os olhos do Senhor Lobo brilharem. Mas apesar da deliciosa comida e do aconchegante ambiente, uma sensação de desconfiança pairava no ar."
            )
            print()
            print(
                f"Após o jantar, enquanto {nome_coelho} estava contemplando a ideia de sair na chuva novamente por causa do pequeno desconforto que pairava o ambiente,\n\
o Senhor Lobo, percebendo sua hesitação, perguntou:\n\
Voce fez um jantar explendido! Obrigado... Está tarde e ainda está chovendo lá fora. Gostaria de passar a noite aqui?"
            )
            print()
            pernoite(nome_coelho)
            salvar_jogo("escolha_pernoite", nome_coelho)

        elif escolhas_jantar[escolha] == "recusar":
            print(f"{nome_coelho} agradece, mas diz que não está com fome.")
            print()
            print(
                "Ele te achou mal agradecido(a), se sentiu ofendido com a recusa e começou a te caçar pela casa até te matar. (VERMELHO)\n\
    \nVOCE PERDEU.\n"
            )
        elif escolhas_jantar[escolha] == "salvar_e_voltar_ao_menu":
            salvar_jogo("jantar_em_andamento", nome_coelho)
            print("Jogo salvo com sucesso! Voltando ao menu inicial.")
            return
        else:
            print("Opção inválida.")


def pernoite(nome_coelho):
    escolhas_pernoite = {
        "1": "aceitar",
        "2": "recusar_e_levantar",
        "3": "recusar_e_perguntar",
        "4": "salvar_e_voltar_ao_menu",
    }

    print(
        "1. Agradecer e dizer que vai ficar.\n"
        "2. Dizer que não e levantar-se para se retirar\n"
        "3. Gentilmente recusar e perguntar se já pode ir embora.\n"
        "4. Salvar e voltar ao menu inicial.\n"
    )
    escolha = input("O que voce deseja fazer? ")
    print()

    if escolha in escolhas_pernoite:
        print(
            "---------------------------------------------------------------------------------------------------------------------------------------------"
        )
        if escolhas_pernoite[escolha] == "aceitar":
            print(
                f"{nome_coelho} agradeceu a generosidade do Senhor Lobo e aceitou passar a noite em sua residencia."
            )
            print()
            print(
                "O Senhor Lobo, com um sorriso caloroso, o guiou até o quarto de hóspedes, ajudando voce a arrumar a cama para uma noite tranquila. (VERDE)"
            )
            print()
            print(
                f"Antes de se retirar do quarto, o Senhor Lobo deixou um aviso para o coelho:\n\
        SENHOR LOBO: Por favor, a noite esta casa fica bastante escura, então não saia do quarto durante a madrugada. E em hipótese alguma entre no meu escritório. É um lugar muito especial para mim.\n\
{nome_coelho} entende as regras e se despede, o Senhor Lobo retribui, sai do quarto e fecha a porta devagar. {nome_coelho} se deita na cama confortavel e\n\
macia que o Senhor Lobo preparou mas sua curiosidade nao o deixava dormir. O corajoso coelho queria explorar a casa do Senhor Lobo.\n\
entao, ele abre a porta do quarto devagar, desce as escadas e se depara com um corredor iluminado por uma luz suave. No final do corredor\n\
{nome_coelho} avista 3 portas..."
            )
            print()
            explorar_casa(nome_coelho)
            salvar_jogo("explorar_casa", nome_coelho)

        elif escolhas_pernoite[escolha] == "recusar_e_levantar":
            print(
                f"\n{nome_coelho} agradece pelo jantar, mas diz que prefere já ir andando e começa a se levantar."
            )
            print()
            print(
                "Antes que voce perceba o Senhor Lobo está parado na sua frente, bloqueando sua saída. Com um olhar sombrio, ele tranca a porta. Em um movimento\n\
rápido, ele te agarra e te leva para o porão, trancando-o em uma jaula até decidir quando te devorar. (VERMELHO)\n\
\nVOCE PERDEU.\n"
            )

        elif escolhas_pernoite[escolha] == "recusar_e_perguntar":
            print(
                f"\n{nome_coelho} recusa educadamente e pergunta se já pode ir embora."
            )
            print()
            print(
                f'O Senhor Lobo, com um olhar ligeiramente decepcionado, responde:"Infelizmente, acho que voce deve ficar. Não é seguro lá fora nesta hora."\n\
E antes que voce possa protestar, ele se retira, deixando voce sozinho na sala de jantar enquanto sobe as escadas para arrumar a sua cama. (AMARELO)"\n\
{nome_coelho} segue o Senhor Lobo ate o quarto de hóspedes, entra e se deita em sua cama macia preparada pelo anfitrião. {nome_coelho}"\n\
se despede do Senhor Lobo, ele retribui, sai do quarto e fecha a porta devagar. Sua curiosidade nao o deixava dormir. {nome_coelho} queria"\n\
explorar a casa do Senhor Lobo, entao, ele abre a porta do quarto devagar, desce as escadas e se depara com um corredor iluminado\n\
por uma luz suave. No final do corredor {nome_coelho} avista 3 portas..."'
            )
            print()
            explorar_casa()
            salvar_jogo("explorar_casa", nome_coelho)
        elif escolhas_pernoite[escolha] == "salvar_e_voltar_ao_menu":
            salvar_jogo("escolha_pernoite", nome_coelho)
            print("Jogo salvo com sucesso! Voltando ao menu inicial.")
            return
        else:
            print("Opção inválida.")


def explorar_casa(nome_coelho):
    escolhas_explorar_casa = {
        "1": "quarto_senhor_lobo",
        "2": "escritorio_senhor_lobo",
        "3": "porta_misteriosa",
        "4": "voltar_ao_quarto",
        "5": "salvar_e_voltar_ao_menu",
    }

    print(
        "Para onde voce gostaria de ir?\n"
        "1. Abrir a porta que leva ao quarto do Senhor Lobo.\n"
        "2. Tentar a porta que leva ao escritório do Senhor Lobo.\n"
        "3. Investigar a terceira porta, que parece misteriosa.\n"
        "4. Voltar ao quarto.\n"
        "5. Salvar e voltar ao menu inicial\n"
    )

    escolha = input("Escolha a porta que deseja abrir: ")

    if escolha in escolhas_explorar_casa:
        porta = escolhas_explorar_casa[escolha]

        print(
            "---------------------------------------------------------------------------------------------------------------------------------------------"
        )
        if porta == "quarto_senhor_lobo":
            print()
            print(
                f"{nome_coelho} abre a porta do quarto do Senhor Lobo. O quarto está escuro, mas {nome_coelho} pode ouvir a respiração suave do Senhor Lobo enquanto ele dorme.\n\
O coelho entao avista uma fotografia em uma estante do outro lado do quarto e decide se aproximar para ver com mais clareza quem estava naquela imagem...\n\
ele começa a andar cuidadosamente pelo quarto, nas pontas das suas pequenas patas enquanto encara o lobo em seus trajes de dormir e em um sono pesado.\n\
ao chegar na estante e pegar a fotografica em mãos, o coelho nota o Senhor Lobo e um cervo na imagem, abraçados e sorrindo como se fossem velhos amigos\n\
ao virar e olhar a parte de trás da fotografia, {nome_coelho} começou a tremer ao notar que havia um borrão de sangue na ponta da foto e ao lado uma frase escrita com uma\n\
letra elegante: Para aquele a quem eu amo. Ass: Senhor Lobo. o coelho sentiu um arrepio na espinha e entao decidiu por a fotografica no lugar e sair do quarto... mas de repente\n\
{nome_coelho} se assusta ao ouvir um som estranho vindo da cama e ao encarar o lobo novamente ele nota uma silhueta em pé com os olhos vermelhos o encarando. alí o coelho ja\n\
sabia que era o seu fim. Ele tentou correr mas rapidamente o Senhor Lobo salta da cama e morde sua garganta, fazendo {nome_coelho} asfixiar em seu próprio sangue até a morte. (VERMELHO)\n\
\nVOCE PERDEU.\n"
            )

        elif porta == "escritorio_senhor_lobo":
            print()
            print(
                f"{nome_coelho} decide tentar a porta que leva ao escritório do Senhor Lobo. Ao abrir a porta, o coelho sente um arrepio na espinha ao olhar ao redor, e entao ele da de cara com\n\
uma cabeça de cervo empalhada em uma das paredes do escritório, um tapete de urso ao centro da sala, ao lado da mesa um casaco de pele de raposa em um cabideiro e um elegante sapato que\n\
parecia ser de couro de cobra. {nome_coelho} estava suando frio ao pensar que poderia ser ele o proximo a morrer e se tornar a mais nova aquisição da coleção do Senhor Lobo...\n\
ao se aproximar da prateleira de livros com suas pernas bambas, o coelho notou uma série de livros ao final da prateleira, enumerados de 1 a 5, onde o livro de número 2 havia uma pequena\n\
mancha e um arranhao em sua borda. {nome_coelho} estava atonito entao apenas ignorou e seguiu em frente em direção a mesa.\n\
    Ao pisar no tapete de urso ele notou um rangido vindo a baixo da cabeça do urso... ao levantar o tapete pesado e espesso {nome_coelho} notou uma ripa de madeira em falso e ao levanta-la\n\
ele achou uma fotografia de uma família alegre, nela havia a mamãe e o papai lobo e logo ao centro um pequeno lobinho sorridente que ao bater os olhos o coelho o reconheceu como o Senhor Lobo.\n\
Ao virar a foto {nome_coelho} avista uma data: 17/01. O pequeno coelho nao entendeu o porquê da foto estar ali mas achou a imagem muito bonita, entao ele a botou no lugar e voltou a vasculhar a sala.\n\
    O coelho ao reparar melhor na cabeça do cervo, reparou que havia algo escrito em sua moldura entao se aproximou para poder ler: Kalvin 8... 'o nome dele era Kalvin?' pensava {nome_coelho} sem chegar\n\
a nenhuma conclusão, ele nao parava de tremer e sentir que o perigo estava a alguns passos de distancia daquela sala, dormindo, enquanto {nome_coelho} estava onde sabia que nao deveria estar.\n\
assim que chegou na mesa do escritório o coelho notou a mesa totalmente organizada, com um notebook e um calendário em cima da mesma. ao olhar o calemdário o coelho notou que o número 9 de todos\n\
os meses do ano estavam marcados.\nTalvez alguma obcessão com o número 9? Número da sorte? - se perguntou o coelho. ao mexer nas gavetas da mesa ele achou um pequeno cofre eletronico que estava pedindo\n\
uma senha de 4 digitos e muito curioso ele decide tentar o abrir e ver o que poderia ter dentro..."
            )
            print()
            senha_cofre(nome_coelho)
        elif porta == "porta_misteriosa":
            print(
                f"{nome_coelho} sente uma curiosidade irresistível em relação à terceira porta. Ao abri-la, o pequeno coelho se depara com uma escadaria que\n\
o levam para uma parte misteriosa da casa no qual ele não faz ideia de o que é.\n\
    Descendo as velhas escadas de madeira com todo o cuidado para não fazer barulho, o coelho sente seu coração acelerando, como se o seu extinto o tivesse implorando para retornar ao quarto\n\
mas sua curiosidade não o permitiria tomar tal decisão. {nome_coelho} desce as escadas e encontra um completo breu até que avista uma pequena corrente ligada a uma lâmpada no teto e a puxa para que\n\
a luz ilumine o ambiente. Assim que a luz ilumina o ambiente, {nome_coelho} avista o que parece ser um sombrio porão, repleto de jaulas enferrujadas e objetos estranhos. O coelho olha ao redore e vê\n\
várias jaulas vazias, algumas delas com sinais de uso recente. Em uma delas, ele nota potes que continham comida estragada, resto de palha e manchas suspeitas. Seu coração bate mais rápido à medida\n\
que ele percebe a terrível verdade: o Senhor Lobo usa esse porão para aprisionar e torturar outros animais.\n\
    À medida que {nome_coelho} explora mais, ele avista ganchos enferrujados, correntes penduradas e outros objetos de tortura macabra que fazem seu pequeno corpo tremer de medo.\n\
Ele nota também algumas prateleiras com frascos contendo líquidos estranhos e ferramentas afiadas. O ar no porão é pesado, e o coelho começa a sentir que não está sozinho. E realmente não estava...\n\
Ele começa a ouvir sussurros suaves e gemidos baixos vindos do fundo do porão, em uma parte mais escuta onde a luz não pode chegar. Seus olhos se ajustam à penumbra, revelando figuras tremeluzentes nas\n\
sombras das jaulas. Outros animais, vítimas do Senhor Lobo, olham para ele com olhos assustados. {nome_coelho} sente o peso da tristeza e do desespero no ar, ecoando nos corredores escuros do porão\n\
    Chegando perto das jaulas ele se depara com uma raposa, um macaco e uma pequena capivara, aprisionados e em condições insalubres proporcionadas pelo anfitrião da casa.\n\
\n      {nome_coelho}: Meu Deus! O que ele fez com vocês?\n\
        RAPOSA: Ele é um monstro! Tortura-nos dia e noite, nos usa para suas exibições macabras.\n\
        MACACO: Por favor, nos tire daqui. Ele vai nos matar, assim como fez com os outros.\n\
        CAPIVARA: Você deve fugir enquanto pode. O Senhor Lobo é impiedoso e sádico.\n\
        {nome_coelho}: Não posso os deixar aqui desse jeito. Preciso encontrar uma maneira de libertá-los, vou ajudar vocês, eu prometo!\n\
\n    Nesse momento, o porão fica silencioso. As pupilas dos animais se fecham ao captarem um movimento atrás de {nome_coelho} e o medo toma conta do ambiente rapidamente.\n\
\n        {nome_coelho}: O que foi?\n\
        RAPOSA: Ele está aqui...\n\
    O coelho vira-se lentamente e se depara com o Senhor Lobo, cujos olhos vermelhos brilham na escuridão.\n\
\n        SENHOR LOBO: Não deveria ter vindo aqui, eu gostei tanto de você... mas voce cometeu um grande erro, pequeno coelhinho. Agora, será parte da minha coleção para sempre.\n\
        {nome_coelho}: Você... Você é um monstro!!\n\
        SENHOR LOBO: Ah, pequeno(a) {nome_coelho}, foi mais rápido do que eu esperava, queria passar mais dias com você... mas no fim apenas estou adicionando mais um à minha coleção. Você será uma peça única.\n\
    E antes que {nome_coelho} consiga desviar, o Senhor Lobo se move com uma rapidez surpreendente, agarrando-o e lançando-o dentro de uma das jaulas. A porta se fecha com um estrondo, deixando o pequeno coelho trancado.\n\
O Senhor Lobo sorri malevolamente enquanto se afasta, deixando {nome_coelho} preso na escuridão da jaula. O coelho passa seus dias restantes naquele lugar sombrio, ouvindo a agonia dos outros animais e esperando seu\n\
destino final, que é se tornar mais uma horrenda obra de arte nas mãos do Senhor Lobo. O porão silencioso se torna o seu cárcere, e a esperança de escapar desvanece enquanto a escuridão consome tudo ao seu redor. (VERMELHO)\n\
\nVOCÊ PERDEU\n"
            )

        elif porta == "voltar_ao_quarto":
            print(
                f"{nome_coelho} decide não explorar e volta ao quarto. Talvez seja melhor descansar antes de continuar a exploração. Ao andar pelo corredor de volta ao seu quarto, o coelho começa a sentir uma presença\n\
assustadora no fim do corredor e ao se aproximar o Senhor Lobo surge das sombras com suas garras afiadas para fora e um olhar assustador e medonho. Ele se move rapidamente arranhando o rosto de {nome_coelho} e o agarrando\n\
pelos braços.\n\
\n        SENHOR LOBO: Você não deveria sair do seu quarto durante a noite, meu pequeno, eu avisei. Que pena... eu tinha tantos planos para você antes de te transformar em uma obra de arte...\n\
\n    O lobo aperta sua presa com força contra a parede e, {nome_coelho}, incapaz de se libertar, se debate em vão enquanto implora por misericórdia.\n\
    E com isso, o Senhor Lobo leva {nome_coelho} para longe, fora da vista, enquanto o corredor fica silencioso novamente, deixando para trás apenas o eco dos gritos abafados do pobre coelho. (VERMELHO)\n\
\nVOCE PERDEU\n"
            )

        elif porta == "salvar_e_voltar_ao_menu":
            salvar_jogo("explorar_casa", nome_coelho)
            print("Jogo salvo com sucesso! Voltando ao menu inicial.")
            return
    else:
        print("Opção inválida.")


def senha_cofre(nome_coelho):
    senha_correta = "2809"
    tentativas_restantes = 3

    while tentativas_restantes > 0:
        try:
            tentativa = input("Digite a senha do cofre (4 dígitos): ")

            tentativa = int(tentativa)

            if 1000 <= tentativa <= 9999:
                if tentativa == int(senha_correta):
                    print(
                        f"Senha correta! O cofre se abre e {nome_coelho} nota uma carta dentro do cofre. O coelho estende o braço para pegar e ao abrir a carta se depara com uma mensagem escrita:\n\
                Não deixe ele gostar demais de você. VÁ EMBORA.\n"
                    )
                    return True, fuga(nome_coelho)
                else:
                    tentativas_restantes -= 1
                    if tentativas_restantes > 0:
                        print(
                            f"MENSAGEM DO COFRE: Senha incorreta. {tentativas_restantes} tentativas restantes."
                        )
                    else:
                        print(
                            "\nMESNAGEM DO COFRE: Você excedeu o número máximo de tentativas. Cofre bloqueado.\n"
                        )
                        print(
                            f"Assim que o coelho digitou a senha errada pela última vez, o cofre soltou uma sirene alta capaz de ser ouvida a centenas de metros de distância. {nome_coelho} tentou correr\n\
        até a porta e escapar da casa de qualquer jeito, mas ao chegar na porta, ele bate de frente com o grande lobo, que o encara com seus olhos vermelhos e furiosos. O coelho, apavorado, gagueja:\n\
                    {nome_coelho}: E-eu... eu... Desculpe, eu queria beber água e então entrei no seu escritório sem querer...\n\
                    SENHOR LOBO: (com uma voz grave e ameaçadora) Você não deveria estar aqui. Este é o meu território. Você violou as regras.\n\
                    {nome_coelho}: Me desculpe, eu não queria cheirar e acorda-lo. Irei voltar para o meu quarto...\n\
                    SENHOR LOBO: (com um rosnado profundo) Tarde demais. Você estragou tudo, coelhinho, eu tinha tantos planos antes de te rasgar e te fazer meu novo troféu... Prepare-se para as consequências.\n\
        Assim que {nome_coelho} ouviu as palavras, o lobo o levantou com força e quebrou seu pescoço com uma imensa facilidade. (VERMELHO)\n\
        \nVOCE PERDEU.\n"
                        )
                        return False
            else:
                print("Erro: A senha deve ser um número de 4 dígitos.")
        except ValueError:
            print("Erro: A senha deve ser um número de 4 dígitos.")

    return False


def fuga(nome_coelho):
    print(
        "--------------------------------------------------------------------------------------------------------"
    )
    print(
        f'O coelho estava atônito, em choque. "Eu estava o tempo todo lidando com um assassino maníaco?" era a única coisa que ele conseguia pensar. Com a mensagem em mãos e vendo o que o Lobo havia feito\n\
com todos aqueles animais em seu escritório, {nome_coelho} decide que não pode ficar mais um segundo na casa do Senhor Lobo. Ele precisa fugir em segurança antes que o lobo o encontre. O coração de {nome_coelho}\n\
batia acelerado enquanto ele corria pelos corredores sombrios, tentando evitar qualquer encontro com o Senhor Lobo. Cada sombra parece ameaçadora, e o coelho estava determinado a não ser capturado.\n\
Ao descer as escadas, {nome_coelho} finalmente chega a porta da sala mas o seu corpo congela. Ele hesita por um momento mas ao ver novamente a carta em suas mãos as palavras escritas vieram em sua cabeça e isso deu forças para que {nome_coelho}\n\
abra a porta e corra em liberdade.\n\
    {nome_coelho} abre rapidamente a porta e corre pelo campo em direção a floresta enquanto pensa nos perigos que o aguardam naquela floresta mas também pensa que nenhum deles se compara ao perigo vivido dentro da casa do lobo.\n\
Adentrando a floresta enquanto corre desesperadamente, {nome_coelho} ouve um uivo distante, ecoando pela floresta...\n\
\n      {nome_coelho}: Será que o lobo está me perseguindo?\n\
    A incerteza só aumenta a determinação do coelho em escapar enquanto fala consigo mesmo no meio de sua respiração ofegante. Ao olhar para trás, ele avista entre as árvores da floresta o chalé do Senhor Lobo, agora distante.\n\
{nome_coelho} vê uma figura escura na porta do chalé, era o lobo com os olhos vermelhos fixos nele. Mas {nome_coelho} não para. Ele continua correndo em direção à liberdade, decidido(a) a deixar para trás o terror que enfrentou naquela casa macabra. (VERDE)\n\
\nVOCE ESCAPOU DAS GARRAS DO SENHOR LOBO.\n'
    )


def main():
    while True:
        menu()
        user_input = input("Escolha uma das opções acima: ")
        match user_input:
            case "1":
                progresso, nome = verificar_progresso_salvo()
                print(f"Progresso: {progresso}, Nome: {nome}")
                jogar(progresso, nome)
            case "2":
                como_jogar()
            case "3":
                print("Obrigado por jogar! Até a próxima.\n")
                break
            case _:
                print("Opçao inválida.")


if __name__ == "__main__":
    main()
