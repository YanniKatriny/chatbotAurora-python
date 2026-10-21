def abertura():
    print()
    print('AURORA: Olá! Eu sou a Aurora, assistente de atendimento '
    'da plataforma Soul Aurora, feita para apoiar terapeutas '
    'integrativos e holísticos que buscam estruturar e expandir a própria prática.')

    print()
    print('AURORA : Antes de começarmos, me diga seu nome?')
    nome = input('')
    nome = nome.upper()

    return nome



def menu_dores(nome):
    print()
    print(f'AURORA: Prazer, {nome}! De acordo com o que mais pesa para você, entenda como a Aurora pode te ajudar.')
    
    print('1 - Estou começando agora')
    print('2 - Transição de carreira sem clientes')
    print('3 - Dificuldade em atrair clientes')
    print('4 - Dificuldade em organizar meus atendimentos')
    escolha = input('ESCOLHA UMA OPÇÃO: ')
    
    return escolha



def resposta_dor(escolha, nome):
    print()
    if escolha == '1':
        print(f'AURORA: Bom, {nome}! Com a Aurora, você já recebe clientes mais conscientes desde o início, que chegam com clareza sobre suas dores, em vez de confusos.')
    
    elif escolha == '2':
        print(f'AURORA: Bom, {nome}! A Aurora te ajuda a sair do improviso: organiza captação, análise emocional e acompanhamento num fluxo só.')
    
    elif escolha == '3':
        print(f'AURORA: Bom, {nome}! A função da Aurora é a captação inteligente, clientes mais preparados chegam até você através da jornada que ela conduz com eles.')
    
    elif escolha == '4':
        print(f'AURORA: Bom, {nome}! A Aurora estrutura sua prática: sem mais improviso, com captação, análise e acompanhamento integrados.')

    else:
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
        escolha = menu_dores(nome)
        resposta_dor(escolha, nome)



def menu_aprofundamento(nome):
    print()
    print(f'AURORA: Para aprofundar, sobre o que mais gostaria de saber, {nome}?')
    
    print('1 - Quem é a Aurora?')
    print('2 - Como funciona no dia a dia?')
    print('3 - O que é a jornada das 9 camadas?')
    print('4 - Limites: o que a Aurora entrega e o que não faz?')
    print('5 - Planos e preços?')
    print('6 - Sair')
    opcao = input('ESCOLHA UMA OPÇÃO: ')

    return opcao



def resposta_aprofundamento(opcao, nome):
    if opcao == '1':
        quem_e_aurora(nome)
    
    elif opcao == '2':
        como_funciona(nome)
    
    elif opcao == '3':
        jornada_9_camadas(nome)
    
    elif opcao == '4':
        limites_eticos(nome)
    
    elif opcao == '5':
        planos_precos(nome)
    
    elif opcao == '6':
        encerramento(nome)
    
    else: 
        print()
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE.')
        opcao = menu_aprofundamento(nome)
        resposta_aprofundamento(opcao, nome)



def quem_e_aurora(nome):
    print()
    
    print('AURORA: A Aurora é a primeira IA terapêutica do Brasil, integrada a uma plataforma de gestão '
    'para terapeutas integrativos e holísticos. Ela existe para te ouvir, te preparar, e te ajudar a decidir se a plataforma é pra você.')

    qa_menu(nome)



def qa_menu(nome):
    print()
    print('AURORA: Quer saber mais sobre: ')
    print('1 - A Aurora funciona como uma pessoa de verdade?')
    print('2 - Para quais abordagens terapêuticas ela serve?')
    print('3 - Voltar ao menu')
    escolha = input('ESCOLHA UMA OPÇÃO: ')
    
    subperguntas_quem_e_aurora(escolha, nome)



def subperguntas_quem_e_aurora(escolha, nome):
    print()
    if escolha == '1':
        print('AURORA: Não. A Aurora é uma inteligência artificial, ela não finge ser humana. '
        'Ela sabe e diz o que ela é.') 
    
    elif escolha == '2':
        print('AURORA: Ela foi construída para terapia integrativa e holística. '
        'Atende bem reiki, florais, constelação, aromaterapia, cromoterapia e demais práticas integrativas.')

    elif escolha == '3':
        opcao = menu_aprofundamento(nome)
        resposta_aprofundamento(opcao, nome)
        return

    else: 
        print()
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
        qa_menu(nome)
        return

    qa_ver_outra(nome)



def qa_ver_outra(nome):
    print()
    print(f'AURORA: Gostaria de ver a outra pergunta sobre "Quem é a Aurora", {nome}?')
    print('1 - Sim')
    print('2 - Não')
    ver_outra = input('ESCOLHA UMA OPÇÃO: ')
    
    if ver_outra == '1':
        qa_menu(nome)
    
    elif ver_outra == '2':
        perguntar_continuar(nome)

    else:
        print()
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
        qa_ver_outra(nome)



def como_funciona(nome):
    print()
    print('AURORA: A Aurora atua em duas partes no dia a dia: antes de qualquer sessão ao acolher seu cliente que chega pelo seu link, e durante o '
    'vínculo que você já construiu com ele, ela também conduz esse cliente por uma jornada '
    'de escuta em camadas antes do primeiro encontro com você. Com o seu link circulando a Aurora irá acolher todos os ' 
    'seus clientes que chegarem 24 horas por dia. Você divulga o link, ela acolhe.')


    print()
    print('AURORA: Quer entender melhor sobre: ')
    print('1 - Como funciona a divulgação?')
    print('2 - Voltar ao menu')
    escolha = input('ESCOLHA UMA OPÇÃO: ')

    subperguntas_como_funciona(escolha, nome)



def subperguntas_como_funciona(escolha, nome):
    print()
    if escolha == '1':
        print('AURORA: A divulgação é feita por você: você compartilha o link da Aurora nas sua redes sociais, ' 
        'WhatsApp ou site. Quando o seu cliente clica nesse link, ele entra em contato direto com a Aurora, ' 
        'que o acolhe numa conversa, ouvindo o que pesa pra ele antes da primeira sessão com você. ' 
        'No final dessa conversa, a Aurora te devolve tudo o que foi revelado, organizado num relatório,  ' 
        'pra você já chegar sabendo onde pisar.')

        perguntar_continuar(nome)

    elif escolha == '2':
        opcao = menu_aprofundamento(nome)
        resposta_aprofundamento(opcao, nome)
        return

    else:
        print()
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE')
        como_funciona(nome)
        

    
def jornada_9_camadas(nome):
    print()
    print('AURORA: É o protocolo que a Aurora conduz com o seu cliente antes da primeira sessão: mapeia o presente, ' 
    'desce à raiz do padrão que se repete, e integra onde o corpo registra e como seria a vida em equilíbrio. ')

    jornada_menu(nome)



def jornada_menu(nome):
    print()
    print('AURORA: Quer saber mais sobre: ')
    print('1 - O cliente já chega "pronto" pra terapia?')
    print('2 - O que recebo no final da jornada dele?')
    print('3 - Voltar ao menu')
    escolha = input('ESCOLHA UMA OPÇÃO: ')

    subperguntas_jornada(escolha, nome)



def subperguntas_jornada(escolha, nome): 
    print()
    if escolha == '1':
        print('AURORA: Não chega curado, chega mais consciente. Antes de te procurar, ele já foi conduzido por uma ' 
        'escuta em camadas: primeiro mapeou onde dói e como isso aparece no dia a dia dele, depois desceu ' 
        'até o padrão que se repete, até a raiz. Isso não resolve nada sozinho, mas tira o peso bruto da ' 
        'primeira fala, e a sua sessão já começa de um lugar mais fundo, sem precisar gastar tempo só destravando o começo.')

    elif escolha == '2':
        print('AURORA: Você recebe o Mini Relatório da Consciência, um retrato organizado do que essa pessoa revelou ' 
        'durante a jornada: a área que mais pesa pra ela, a emoção que sustenta esse peso, o padrão que se repete, ' 
        'e a frase interna que ela carrega sobre isso. Não é um resumo genérico, é o material da escuta, ' 
        'organizado pra você já saber onde pisar antes mesmo do primeiro "oi".')

    elif escolha == '3':
        opcao = menu_aprofundamento(nome)
        resposta_aprofundamento(opcao, nome)
        return

    else:
        print()
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
        jornada_menu(nome)
        return
        
    jorn_ver_outra(nome)



def jorn_ver_outra(nome):
    print()
    print(f'AURORA: Gostaria de ver a outra pergunta sobre "A Jornada das 9 camadas", {nome}?')
    print('1 - Sim')
    print('2 - Não')
    ver_outra = input('ESCOLHA UMA OPÇÃO: ')

    if ver_outra == '1':
        jornada_menu(nome)

    elif ver_outra == '2':
        perguntar_continuar(nome)

    else:
        print()
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
        jorn_ver_outra(nome)



def limites_eticos(nome):
    print()
    print('AURORA: A Aurora entrega quatro coisas concretas: ')
    print('1 - Clientes chegam mais preparados, que já passaram por uma investigação emocional estruturada e chegam à primeira ' 
    'sessão com clareza sobre suas dores. ')
    print('2 - Mais segurança na condução, com acesso a padrões emocionais organizados depois da jornada. ')
    print('3 - A estrutura pra você sair do improviso, integrando captação, análise emocional e acompanhamento num fluxo só. ')
    print('4 - E a possibilidade de atender mais pessoas sem perder a profundidade, porque ela '
    'cuida da triagem emocional enquanto você foca no vínculo e na transformação.')

    limites_menu(nome)



def limites_menu(nome):
    print()
    print('AURORA: Quer saber mais sobre: ')
    print('1 - A Aurora substitui o terapeuta ou faz diagnóstico?')
    print('2 - Meus dados ficam protegidos?')
    print('3 - Voltar ao menu')
    escolha = input('ESCOLHA UMA OPÇÃO: ')

    subperguntas_limites(escolha, nome)



def subperguntas_limites(escolha, nome):
    print()
    if escolha == '1':
        print('AURORA: Não. A Aurora prepara o terreno. A avaliação continua sendo sua, agora com mais material pra sustentá-la. '
    'Ela identifica padrões e raízes simbólicas nos relatórios que entrega, mas diagnóstico é território humano e regulado, ' 
    'e ela respeita esse limite com firmeza. O limite é claro: quem entrega o resultado terapêutico é sempre profissional, ' 
    'a Aurora entrega o terreno preparado.')

    elif escolha == '2':
        print('AURORA: Integralmente. A Aurora é LGPD compliant, com SSL seguro. '
            'Ela não vende, não compartilha, não expõe dados, nem os seus, nem os do seu cliente. ' 
            'Isso faz parte dos três pilares que sustentam a plataforma: ética profissional, privacidade de dados e escuta qualificada.')

    elif escolha == '3':
        opcao = menu_aprofundamento(nome)
        resposta_aprofundamento(opcao, nome)
        return

    else:
        print()
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
        limites_menu(nome)
        return

    lim_ver_outra(nome)



def lim_ver_outra(nome):
    print()
    print(f'AURORA: Gostaria de ver a outra pergunta sobre os limites da Aurora, {nome}?')
    print('1 - Sim')
    print('2 - Não')
    ver_outra = input('ESCOLHA UMA OPÇÃO: ')

    if ver_outra == '1':
        limites_menu(nome)

    elif ver_outra == '2':
        perguntar_continuar(nome)

    else:
        print()
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE')
        lim_ver_outra(nome)



def planos_precos(nome):
    print() 
    print('AURORA: A Aurora tem três portas de entrada: ')
    print('- Essencial, R$ 127,90/mês: captação inteligente + preparação emocional.')
    print('- Profissional, R$ 297,90/mês (o mais escolhido): tudo do Essencial + agendamento, pagamentos, ' 
    'Meet Aurora e Aurora Insight. ')
    print('- Vitalício, R$ 2.997,90 (pagamento único): pra quem aposta de vez. ')
    print()
    print('Garantia de 7 dias: se não for pra você, a Aurora devolve 100%, sem burocracia.')

    planos_menu(nome)



def planos_menu(nome):
    print()
    print(f'AURORA: O que você decide, {nome}?')
    print('1 - Quero assinar')
    print('2 - Quero testar sem riscos')
    print('3 - Voltar ao menu')
    escolha = input('ESCOLHA UMA OPÇÃO: ')

    subperguntas_planos(escolha, nome)



def subperguntas_planos(escolha, nome):
    print()
    if escolha == '1':
        print('AURORA: Você escolhe o plano que combina com você, preenche seus dados de contato '
        'e pagamento na página de assinatura, e em poucos minutos já tem acesso à sua área da Aurora, '
        'pronta pra compartilhar o link com seus clientes.')
        perguntar_continuar(nome)

    elif escolha == '2':
        print('AURORA: Você assina normalmente o plano escolhido, e tem 7 dias de garantia '
        'incondicional pra usar sem risco. Se dentro desse prazo sentir que não é o momento, '
        'é só pedir o reembolso, sem burocracia, sem justificativa, e recebe todo o valor de volta.')
        perguntar_continuar(nome)

    elif escolha == '3':
        opcao = menu_aprofundamento(nome)
        resposta_aprofundamento(opcao, nome)

    else:
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
        planos_menu(nome)



def perguntar_continuar(nome):
    print()
    print(f'AURORA: Ainda tem alguma dúvida, {nome}?')
    print('1 - Sim, quero ver outras opções. ')
    print('2 - Não, pode encerrar aqui.')
    escolha = input('ESCOLHA UMA OPÇÃO: ')
    
    if escolha == '1':
        opcao = menu_aprofundamento(nome)
        resposta_aprofundamento(opcao, nome)
    
    elif escolha == '2':
        encerramento(nome)

    else:
        print()
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
        perguntar_continuar(nome)

    

def encerramento(nome):
    print()
    print(f'AURORA: Obrigada, {nome}. ')
    print()



def principal():
    nome = abertura()
    escolha = menu_dores(nome)
    resposta_dor(escolha, nome)
    opcao = menu_aprofundamento(nome)
    resposta_aprofundamento(opcao, nome)


principal()

