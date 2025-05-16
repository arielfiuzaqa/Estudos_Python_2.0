# Quiz com Interface, Timer e Persistência de Resultados
# Requisitos: tkinter, json, os, time

import os
import time
import json
import threading
import tkinter as tk
from tkinter import messagebox

# Caminho do arquivo que salva resultado (para evitar nova execução)
RESULTADO_ARQUIVO = "resultado.json"

# Simula banco de perguntas
'''
{
    "pergunta": "Texto da pergunta?",
    "alternativas": ["a)", "b)", "c)", "d)"],
    "correta": índice_da_resposta_correta (0 a 3),
    "disciplina": "Nome da Disciplina"
}
'''

perguntas = [

    # QA Fundamentos (Automação Nível Médio)
    {"pergunta": "O que é um teste de regressão?", "alternativas": ["Teste de segurança", "Teste de performance", "Teste que verifica se funcionalidades antigas continuam funcionando", "Teste para encontrar vulnerabilidades"], "correta": 2, "disciplina": "Fundamentos"},
    {"pergunta": "Qual a diferença entre verificação e validação?", "alternativas": ["Verificação ocorre após validação", "Validação verifica bugs", "Verificação avalia requisitos; validação avalia produto final", "Não há diferença"], "correta": 2, "disciplina": "Fundamentos"},
    {"pergunta": "O que é um bug?", "alternativas": ["Funcionalidade esperada", "Erro no sistema", "Relatório de requisitos", "Processo de deploy"], "correta": 1, "disciplina": "Fundamentos"},
    {"pergunta": "O que é um caso de teste?", "alternativas": ["Plano de negócio", "Documento de entrega", "Conjunto de condições para validar uma funcionalidade", "Script de automação"], "correta": 2, "disciplina": "Fundamentos"},
    {"pergunta": "O que define um bom caso de teste?", "alternativas": ["Complexidade", "Clareza, reprodutibilidade e cobertura", "Quantidade de linhas de código", "Execução rápida"], "correta": 1, "disciplina": "Fundamentos"},
    {"pergunta": "Qual é o principal objetivo do teste de software?", "alternativas": ["Garantir que o sistema funcione perfeitamente", "Detectar e corrigir todos os bugs", "Verificar se o software atende aos requisitos e encontrar falhas", "Automatizar todos os processos"], "correta": 2, "disciplina": "Fundamentos"},
    {"pergunta": "O que é um teste exploratório?", "alternativas": ["Teste baseado em casos escritos", "Teste que explora funcionalidades desconhecidas para descobrir falhas", "Teste focado em segurança", "Teste realizado por scripts automáticos"], "correta": 1, "disciplina": "Fundamentos"},
    {"pergunta": "Qual o papel do QA em um time ágil?", "alternativas": ["Apenas validar código final", "Corrigir bugs de produção", "Garantir a qualidade durante todo o ciclo de desenvolvimento", "Apenas automatizar os testes"], "correta": 2, "disciplina": "Fundamentos"},
    {"pergunta": "O que são critérios de aceitação?", "alternativas": ["Requisitos técnicos", "Regras para desenvolvimento backend", "Condições que determinam se uma funcionalidade está pronta", "Listagem de bugs conhecidos"], "correta": 2, "disciplina": "Fundamentos"},
    {"pergunta": "Qual técnica visa cobrir todas as combinações possíveis de entradas e saídas?", "alternativas": ["Particionamento de equivalência", "Análise de valor limite", "Tabela de decisão", "Teste de sanidade"], "correta": 2, "disciplina": "Fundamentos"},
    {"pergunta": "O que é um teste de caixa preta?", "alternativas": ["Teste baseado em lógica de código", "Teste sem considerar a estrutura interna do sistema", "Teste de performance", "Teste de segurança em APIs"], "correta": 1, "disciplina": "Fundamentos"},
    {"pergunta": "Teste de sanidade tem como objetivo:", "alternativas": ["Verificar requisitos não funcionais", "Validar integração entre sistemas", "Verificar rapidamente se o sistema está minimamente funcional", "Executar teste de carga"], "correta": 2, "disciplina": "Fundamentos"},
    {"pergunta": "O que é um defeito (defect)?", "alternativas": ["Erro no ambiente de produção", "Bug relatado no GitHub", "Falha que ocorre por um erro no código ou nos requisitos", "Falha de infraestrutura"], "correta": 2, "disciplina": "Fundamentos"},
    {"pergunta": "Qual o objetivo de um plano de teste?", "alternativas": ["Organizar a entrega dos sprints", "Controlar mudanças de código", "Definir escopo, estratégia e cronograma de testes", "Criar banco de dados de testes"], "correta": 2, "disciplina": "Fundamentos"},
    {"pergunta": "O que é teste de aceitação do usuário (UAT)?", "alternativas": ["Teste feito por desenvolvedores", "Teste de carga no ambiente de QA", "Teste feito por usuários finais para validar requisitos", "Teste feito por analistas de infraestrutura"], "correta": 2, "disciplina": "Fundamentos"},
    {"pergunta": "Teste de integração avalia:", "alternativas": ["Funcionamento individual de componentes", "Performance de um componente", "Interação entre diferentes módulos ou sistemas", "Layout visual do sistema"], "correta": 2, "disciplina": "Fundamentos"},
    {"pergunta": "Qual é o tipo de teste feito para verificar se algo que funcionava ainda funciona?", "alternativas": ["Teste unitário", "Teste de performance", "Teste de regressão", "Teste de carga"], "correta": 2, "disciplina": "Fundamentos"},
    {"pergunta": "O que caracteriza um teste negativo?", "alternativas": ["Validar apenas cenários de sucesso", "Forçar o sistema com entradas inválidas ou inesperadas", "Testar apenas tempo de resposta", "Ignorar erros conhecidos"], "correta": 1, "disciplina": "Fundamentos"},
    {"pergunta": "Quais são os três pilares do teste de software?", "alternativas": ["Segurança, usabilidade e escalabilidade", "Código, dados e performance", "Verificação, validação e documentação", "Planejamento, execução e avaliação"], "correta": 3, "disciplina": "Fundamentos"},
    {"pergunta": "O que é teste baseado em risco?", "alternativas": ["Teste voltado apenas para falhas graves", "Planejamento de testes com foco nas áreas mais críticas do sistema", "Teste de segurança em APIs", "Simulação de falhas de infraestrutura"], "correta": 1, "disciplina": "Fundamentos"},
    {"pergunta": "O que é teste de carga?","alternativas": ["Teste para avaliar segurança de dados", "Teste de performance em múltiplas máquinas", "Teste que verifica comportamento sob número crescente de usuários", "Teste de aceitação do cliente"],"correta": 2,"disciplina": "Fundamentos"},
    {"pergunta": "Quando aplicar teste de usabilidade?","alternativas": ["Antes de codificar qualquer sistema", "Durante testes de API", "Para avaliar experiência do usuário final", "Após testes de stress"],"correta": 2,"disciplina": "Fundamentos"},
    {"pergunta": "O que é teste de performance?","alternativas": ["Verifica usabilidade", "Mede tempo de resposta e escalabilidade", "Analisa bugs críticos", "Valida integração de APIs"],"correta": 1,"disciplina": "Fundamentos"},
    {"pergunta": "Qual o foco de um teste de segurança?","alternativas": ["Detectar falhas de interface", "Avaliar consumo de memória", "Identificar vulnerabilidades como SQL Injection", "Testar janelas modais"],"correta": 2,"disciplina": "Fundamentos"},
    {"pergunta": "O que é teste funcional?","alternativas": ["Verifica visual de componentes", "Valida requisitos funcionais especificados", "Simula tráfego pesado", "Verifica documentação do projeto"],"correta": 1,"disciplina": "Fundamentos"},
    {"pergunta": "Qual o objetivo dos testes não-funcionais?","alternativas": ["Testar regras de negócio", "Testar usabilidade, performance, segurança", "Ajustar código-fonte", "Corrigir alertas de log"],"correta": 1,"disciplina": "Fundamentos"},
    {"pergunta": "Quando um bug é considerado crítico?","alternativas": ["Quando causa lentidão ocasional", "Quando impede uso da funcionalidade principal do sistema", "Quando está documentado", "Quando o QA encontra"],"correta": 1,"disciplina": "Fundamentos"},
    {"pergunta": "Como é classificada uma falha que afeta poucos usuários e tem solução alternativa?","alternativas": ["Crítica", "Alta", "Média", "Baixa"],"correta": 3,"disciplina": "Fundamentos"},
    {"pergunta": "O que representa cobertura de testes?","alternativas": ["Porcentagem de testes automatizados", "Quantidade de linhas testadas em relação ao total de código", "Quantidade de pessoas que testaram", "Tempo de execução dos testes"],"correta": 1,"disciplina": "Fundamentos"},
    {"pergunta": "Teste de compatibilidade avalia:","alternativas": ["Conformidade de requisitos", "Execução em diferentes ambientes e dispositivos", "Performance da aplicação", "Integração de serviços"],"correta": 1,"disciplina": "Fundamentos"},
    {"pergunta": "O que significa TDD?","alternativas": ["Testing Done by Developers", "Test Design Diagram", "Test-Driven Development", "Time Dependent Debugging"],"correta": 2,"disciplina": "Fundamentos"},
    {"pergunta": "No TDD, o teste é escrito:","alternativas": ["Após implementar o código", "Durante o planejamento do projeto", "Antes da implementação do código", "Somente em produção"],"correta": 2,"disciplina": "Fundamentos"},
    {"pergunta": "Smoke test é usado para:","alternativas": ["Verificar falhas críticas rapidamente", "Avaliar segurança da aplicação", "Testar banco de dados", "Executar testes de stress"],"correta": 0,"disciplina": "Fundamentos"},
    {"pergunta": "Qual o foco de um teste unitário?","alternativas": ["Verificar sistema inteiro", "Validar módulos ou funções isoladas", "Testar múltiplos dispositivos", "Executar scripts SQL"],"correta": 1,"disciplina": "Fundamentos"},
    {"pergunta": "O que significa BDD?","alternativas": ["Bug-Driven Development", "Behavior-Driven Development", "Base de Dados Dinâmica", "Behavior Data Design"],"correta": 1,"disciplina": "Fundamentos"},
    {"pergunta": "Qual ferramenta é comumente usada para BDD em Python?","alternativas": ["Robot Framework", "Behave", "Selenium", "Jest"],"correta": 1,"disciplina": "Fundamentos"},
    {"pergunta": "O que é Gherkin?","alternativas": ["Ferramenta de automação", "Linguagem usada para escrever cenários de testes BDD", "Protocolo de segurança de testes", "Framework para integração contínua"],"correta": 1,"disciplina": "Fundamentos"},
    {"pergunta": "Quando usar testes manuais?","alternativas": ["Para cenários repetitivos", "Em testes exploratórios e validação visual", "Em testes de stress", "Somente quando não há QA"],"correta": 1,"disciplina": "Fundamentos"},
    {"pergunta": "Quem é responsável pela qualidade no time ágil?","alternativas": ["Apenas o QA", "O gerente de produto", "Toda a equipe", "A liderança técnica"],"correta": 2,"disciplina": "Fundamentos"},
    {"pergunta": "O que é uma falha intermitente?","alternativas": ["Erro constante", "Bug visual", "Falha que ocorre de forma não previsível", "Bug de performance"],"correta": 2,"disciplina": "Fundamentos"},

    # Selenium / Automação Web
    {"pergunta": "Qual comando do Selenium localiza elemento por ID?", "alternativas": ["find_element_by_class", "find_element_by_name", "find_element_by_xpath", "find_element_by_id"], "correta": 3, "disciplina": "Selenium"},
    {"pergunta": "Como realizar um clique em elemento com Selenium?", "alternativas": ["element.type()", "element.send_keys()", "element.click()", "element.enter()"], "correta": 2, "disciplina": "Selenium"},
    {"pergunta": "Para preencher um campo com Selenium, usamos:", "alternativas": ["fill()", "click()", "type()", "send_keys()"], "correta": 3, "disciplina": "Selenium"},
    {"pergunta": "O que faz driver.get(url)?", "alternativas": ["Clica em elemento", "Fecha o navegador", "Abre uma URL", "Captura logs"], "correta": 2, "disciplina": "Selenium"},
    {"pergunta": "Como esperar por um elemento ser clicável?", "alternativas": ["driver.wait()", "time.sleep()", "WebDriverWait + expected_conditions", "click() antes do elemento aparecer"], "correta": 2, "disciplina": "Selenium"},
    {"pergunta": "Qual comando fecha o navegador no Selenium?", "alternativas": ["driver.close()", "driver.quit()", "driver.stop()", "driver.end()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como capturar o texto de um elemento no Selenium?", "alternativas": ["element.get_text()", "element.text", "element.value", "element.get_value()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Qual comando tira um screenshot no Selenium?", "alternativas": ["driver.screenshot()", "driver.save_screenshot()", "driver.capture()", "driver.take_screenshot()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como alternar para um iframe no Selenium?", "alternativas": ["driver.switch_to.frame()", "driver.iframe()", "driver.enter_frame()", "driver.switch_frame()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como verificar se um elemento está visível no Selenium?", "alternativas": ["element.is_displayed()", "element.is_visible()", "element.is_present()", "element.is_enabled()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como rolar a página para um elemento no Selenium?", "alternativas": ["driver.scroll_to()", "element.scroll_into_view()", "driver.execute_script('scroll')", "element.scroll()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como selecionar um valor em um dropdown no Selenium?", "alternativas": ["dropdown.select_by_value()", "dropdown.choose()", "dropdown.pick()", "dropdown.select()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o título da página no Selenium?", "alternativas": ["driver.get_title()", "driver.title", "driver.page_title()", "driver.get_page_title()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como aceitar um alerta no Selenium?", "alternativas": ["driver.alert.accept()", "driver.switch_to.alert.accept()", "driver.alert.confirm()", "driver.switch_to.alert.confirm()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como maximizar a janela do navegador no Selenium?", "alternativas": ["driver.maximize()", "driver.maximize_window()", "driver.fullscreen()", "driver.window_maximize()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o atributo de um elemento no Selenium?", "alternativas": ["element.get_attribute()", "element.attribute()", "element.get_property()", "element.property()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como verificar se um elemento está habilitado no Selenium?", "alternativas": ["element.is_enabled()", "element.is_active()", "element.is_present()", "element.is_visible()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como alternar para uma nova aba no Selenium?", "alternativas": ["driver.switch_to.tab()", "driver.switch_to.window()", "driver.change_tab()", "driver.new_tab()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como simular pressionar uma tecla no Selenium?", "alternativas": ["driver.send_keys()", "element.send_keys()", "driver.press_key()", "element.press_key()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o URL atual no Selenium?", "alternativas": ["driver.get_url()", "driver.current_url", "driver.url()", "driver.page_url()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como esperar por um elemento no Selenium?", "alternativas": ["WebDriverWait", "time.sleep()", "driver.wait_for_element()", "driver.wait()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como fechar uma aba específica no Selenium?", "alternativas": ["driver.close_tab()", "driver.close()", "driver.quit_tab()", "driver.quit()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o tamanho de um elemento no Selenium?", "alternativas": ["element.size", "element.get_size()", "element.dimension()", "element.get_dimension()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o CSS de um elemento no Selenium?", "alternativas": ["element.get_css()", "element.get_style()", "element.value_of_css_property()", "element.css_property()"], "correta": 2, "disciplina": "Selenium"},
    {"pergunta": "Como verificar se um elemento existe no Selenium?", "alternativas": ["driver.find_element()", "driver.find_element_or_none()", "driver.element_exists()", "driver.find_element_by_id()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como alternar para a janela principal no Selenium?", "alternativas": ["driver.switch_to.default_content()", "driver.switch_to.main_window()", "driver.switch_to.root()", "driver.switch_to.parent_window()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o número de abas abertas no Selenium?", "alternativas": ["len(driver.window_handles)", "driver.get_tabs()", "driver.count_tabs()", "driver.tabs_count()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o estado de carregamento da página no Selenium?", "alternativas": ["driver.page_load_state()", "driver.execute_script('return document.readyState')", "driver.page_ready()", "driver.is_page_loaded()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o tipo de elemento no Selenium?", "alternativas": ["element.tag_name", "element.get_tag()", "element.type()", "element.get_type()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o valor de um campo no Selenium?", "alternativas": ["element.get_value()", "element.value", "element.get_attribute('value')", "element.get_property('value')"], "correta": 2, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o texto de um alerta no Selenium?", "alternativas": ["driver.alert.text", "driver.switch_to.alert.text", "driver.get_alert_text()", "driver.alert_message()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o tempo de carregamento da página no Selenium?", "alternativas": ["driver.get_load_time()", "driver.execute_script('return performance.timing')", "driver.page_load_time()", "driver.get_performance()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como verificar se um elemento está selecionado no Selenium?", "alternativas": ["element.is_selected()", "element.is_checked()", "element.is_active()", "element.is_enabled()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o ID de uma janela no Selenium?", "alternativas": ["driver.window_id", "driver.current_window_handle", "driver.get_window_id()", "driver.get_handle()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o histórico de navegação no Selenium?", "alternativas": ["driver.history", "driver.get_history()", "driver.execute_script('return history')", "driver.browser_history()"], "correta": 2, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o tempo de resposta de uma requisição no Selenium?", "alternativas": ["driver.get_response_time()", "driver.execute_script('return performance.timing.responseEnd')", "driver.response_time()", "driver.get_timing()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o tamanho da janela no Selenium?", "alternativas": ["driver.get_window_size()", "driver.window_size", "driver.get_size()", "driver.size()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o foco atual no Selenium?", "alternativas": ["driver.current_focus", "driver.switch_to.active_element", "driver.get_focus()", "driver.active_element()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o tempo de execução de um script no Selenium?", "alternativas": ["driver.execute_script('return performance.now()')", "driver.get_execution_time()", "driver.script_time()", "driver.get_timing()"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o status de uma requisição no Selenium?", "alternativas": ["driver.get_status()", "driver.execute_script('return performance.getEntries()')", "driver.request_status()", "driver.get_request_status()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como verificar o tempo de carregamento de um recurso no Selenium?", "alternativas": ["driver.get_resource_time()", "driver.execute_script('return performance.getEntriesByType('resource')')", "driver.resource_time()", "driver.get_timing()"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Qual a diferença entre `find_element` e `find_elements`?", "alternativas": ["Nenhuma, são sinônimos", "O primeiro retorna o primeiro elemento, o segundo uma lista", "O primeiro busca por ID, o segundo por classe", "O primeiro é mais rápido"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "O que é um `WebDriver`?", "alternativas": ["Um tipo de navegador", "A classe base para todos os elementos", "Uma interface para controlar navegadores", "Um servidor de testes"], "correta": 2, "disciplina": "Selenium"},
    {"pergunta": "Como inspecionar elementos dinâmicos?", "alternativas": ["Usar o inspetor do Chrome e pausar o JavaScript", "Adivinhar o XPath", "Desabilitar o JavaScript", "Usar o Selenium IDE"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Qual a melhor forma de usar `time.sleep()`?", "alternativas": ["Em todo lugar", "Nunca, usar `WebDriverWait`", "Só em testes locais", "Quando o elemento demora muito para carregar"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "Como lidar com pop-ups?", "alternativas": ["Desabilitar pop-ups no navegador", "Usar `driver.switch_to.alert`", "Ignorar", "Fechar manualmente"], "correta": 1, "disciplina": "Selenium"},
    {"pergunta": "O que é Page Object Model (POM)?", "alternativas": ["Um padrão de projeto para organizar elementos e ações", "Um tipo de teste", "Uma forma de gerar relatórios", "Um framework de Selenium"], "correta": 0, "disciplina": "Selenium"},
    {"pergunta": "Como executar JavaScript no Selenium?", "alternativas": ["`driver.run_script()`", "Não é possível", "`driver.execute_script()`", "`driver.javascript()`"], "correta": 2, "disciplina": "Selenium"},

    # Robot Framework
    {"pergunta": "Qual biblioteca do Robot é usada para testes web?", "alternativas": ["RequestsLibrary", "SSHLibrary", "SeleniumLibrary", "ExcelLibrary"], "correta": 2, "disciplina": "Robot Framework"},
    {"pergunta": "Comando Robot para clicar em elemento:", "alternativas": ["Click", "Click Button", "Click Element", "ClickOn"], "correta": 2, "disciplina": "Robot Framework"},
    {"pergunta": "Como definir variáveis no Robot?", "alternativas": ["# VAR", "@var", "${variavel}", "$var"], "correta": 2, "disciplina": "Robot Framework"},
    {"pergunta": "Qual comando inicia o navegador no Robot?", "alternativas": ["Open Page", "Run Browser", "Open Browser", "Start Web"], "correta": 2, "disciplina": "Robot Framework"},
    {"pergunta": "Como rodar testes Robot no terminal?", "alternativas": ["robot arquivo.robot", "run arquivo.robot", "robot.run", "python robot"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Qual a extensão de um arquivo de teste no Robot Framework?", "alternativas": [".rbt", ".robot", ".rf", ".test"], "correta": 1, "disciplina": "Robot Framework"},
    {"pergunta": "O que são Keywords no Robot Framework?", "alternativas": ["Variáveis globais", "Funções ou ações reutilizáveis", "Comentários", "Tipos de dados"], "correta": 1, "disciplina": "Robot Framework"},
    {"pergunta": "Como importar uma biblioteca no Robot Framework?", "alternativas": ["Import Library NomeDaBiblioteca", "Library: NomeDaBiblioteca", "Resource NomeDaBiblioteca.robot", "***Settings***\nLibrary  NomeDaBiblioteca"], "correta": 3, "disciplina": "Robot Framework"},
    {"pergunta": "Qual a sintaxe para um loop FOR no Robot Framework?", "alternativas": ["FOR item IN lista", ":FOR ${item} IN @{lista}", "FOR ${item} IN RANGE 1 10", ":FOR  ${item}  IN  @{lista}"], "correta": 3, "disciplina": "Robot Framework"},
    {"pergunta": "Como verificar se um texto está presente em uma página no Robot Framework?", "alternativas": ["Page Should Contain", "Should See Text", "Verify Text Present", "Text Should Be"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como passar argumentos para uma Keyword customizada?", "alternativas": ["Usando ${argumento}", "Usando @argumento", "Usando &argumento", "Usando #argumento"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Qual comando fecha o navegador no Robot Framework?", "alternativas": ["Close Browser", "End Browser", "Quit Browser", "Stop Browser"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como executar apenas um teste específico em um arquivo .robot?", "alternativas": ["robot -t 'Nome do Teste' arquivo.robot", "robot --only 'Nome do Teste' arquivo.robot", "robot -run 'Nome do Teste' arquivo.robot", "robot -testcase 'Nome do Teste' arquivo.robot"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como reutilizar código entre arquivos .robot?", "alternativas": ["Usando ***Settings*** Resource", "Usando ***Variables***", "Usando ***Test Cases***", "Usando ***Keywords***"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como validar se um elemento está visível na página?", "alternativas": ["Element Should Be Visible", "Element Is Visible", "Check Element Visible", "Element Visible"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como inserir texto em um campo no Robot Framework?", "alternativas": ["Input Text", "Type Text", "Send Keys", "Write Text"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como executar um teste em múltiplos navegadores?", "alternativas": ["Usando variável ${BROWSER}", "Usando argumento --browser", "Usando argumento -v BROWSER", "Todas as anteriores"], "correta": 3, "disciplina": "Robot Framework"},
    {"pergunta": "Como fazer upload de arquivo com Robot Framework?", "alternativas": ["Choose File", "Upload File", "Send File", "Attach File"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como aguardar um elemento aparecer na página?", "alternativas": ["Wait Until Element Is Visible", "Wait For Element", "Wait Element", "Wait Until Visible"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como executar código Python dentro de um teste Robot?", "alternativas": ["Run Keyword", "Evaluate", "Execute Python", "Run Python"], "correta": 1, "disciplina": "Robot Framework"},
    {"pergunta": "Como criar uma variável global em Robot Framework?", "alternativas": ["***Variables***", "***Settings***", "***Globals***", "***Resources***"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como marcar um teste como esperado para falhar?", "alternativas": ["[ExpectedFailure]", "[Fail]", "[Tags] expected_failure", "[Tags] known issue"], "correta": 2, "disciplina": "Robot Framework"},
    {"pergunta": "Como rodar testes em paralelo com Robot Framework?", "alternativas": ["robot --parallel", "pabot", "robot --threads", "robot --multi"], "correta": 1, "disciplina": "Robot Framework"},
    {"pergunta": "Como acessar o valor de uma célula em uma tabela HTML?", "alternativas": ["Get Table Cell", "Table Cell Value", "Get Element Attribute", "Get Table Value"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como verificar se um checkbox está marcado?", "alternativas": ["Checkbox Should Be Selected", "Checkbox Is Checked", "Check Checkbox", "Verify Checkbox"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como executar um teste com diferentes dados de entrada?", "alternativas": ["Data Driven", "Test Template", "For Loop", "Test Data"], "correta": 1, "disciplina": "Robot Framework"},
    {"pergunta": "Como adicionar tags a um teste?", "alternativas": ["[Tags]", "[TestTags]", "[Labels]", "[TestCaseTags]"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como capturar um screenshot em caso de falha?", "alternativas": ["Capture Page Screenshot", "Take Screenshot", "Screenshot On Fail", "Save Screenshot"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como executar um comando de sistema operacional?", "alternativas": ["Run", "Execute", "Run Process", "System Command"], "correta": 2, "disciplina": "Robot Framework"},
    {"pergunta": "Como verificar o valor de um atributo de elemento?", "alternativas": ["Get Element Attribute", "Element Attribute", "Check Attribute", "Verify Attribute"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como limpar um campo de texto antes de digitar?", "alternativas": ["Clear Element Text", "Clear Text", "Empty Field", "Reset Field"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como executar testes em modo headless?", "alternativas": ["--headless", "--no-gui", "--silent", "--background"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como verificar se um elemento não existe na página?", "alternativas": ["Element Should Not Be Visible", "Element Should Not Exist", "Element Not Present", "Check Not Exist"], "correta": 1, "disciplina": "Robot Framework"},
    {"pergunta": "Como pausar a execução para depuração?", "alternativas": ["Pause Execution", "Sleep", "Wait", "Debug"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como obter o texto de um elemento?", "alternativas": ["Get Text", "Element Text", "Read Text", "Fetch Text"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como executar um teste com múltiplos arquivos de dados?", "alternativas": ["Data Files", "Variable Files", "Resource Files", "Test Data"], "correta": 1, "disciplina": "Robot Framework"},
    {"pergunta": "Como verificar o título da página?", "alternativas": ["Title Should Be", "Check Title", "Verify Page Title", "Page Title"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como executar uma Keyword apenas se uma condição for verdadeira?", "alternativas": ["Run Keyword If", "If Keyword", "Conditional Run", "Keyword If"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como obter o valor de uma variável de ambiente?", "alternativas": ["Get Environment Variable", "Read Env", "Env Var", "Get Env"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como verificar se um alerta está presente?", "alternativas": ["Alert Should Be Present", "Check Alert", "Verify Alert", "Alert Present"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como aceitar um alerta/modal?", "alternativas": ["Handle Alert", "Accept Alert", "Confirm Alert", "Alert Accept"], "correta": 1, "disciplina": "Robot Framework"},
    {"pergunta": "Como executar uma Keyword várias vezes?", "alternativas": ["Repeat Keyword", "Run Keyword Multiple Times", "Loop Keyword", "Repeat"], "correta": 1, "disciplina": "Robot Framework"},
    {"pergunta": "Como verificar se um elemento está habilitado?", "alternativas": ["Element Should Be Enabled", "Check Enabled", "Verify Enabled", "Is Enabled"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como obter o valor selecionado em um dropdown?", "alternativas": ["Get Selected List Label", "Get Dropdown Value", "Selected Option", "Dropdown Selected"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como executar testes com diferentes perfis de usuário?", "alternativas": ["User Profiles", "Variable Files", "Test Template", "Resource Files"], "correta": 1, "disciplina": "Robot Framework"},
    {"pergunta": "Como verificar se um elemento está selecionado?", "alternativas": ["Element Should Be Selected", "Check Selected", "Verify Selected", "Is Selected"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como obter o número de elementos encontrados por um locator?", "alternativas": ["Get Element Count", "Count Elements", "Number Of Elements", "Elements Count"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como executar testes em diferentes ambientes (dev, qa, prod)?", "alternativas": ["Usando variável de ambiente", "Usando argumento --variable", "Usando Variable Files", "Todas as anteriores"], "correta": 3, "disciplina": "Robot Framework"},
    {"pergunta": "Como gerar um relatório HTML após execução dos testes?", "alternativas": ["robot gera automaticamente", "robot --report", "robot --output report.html", "robot --html"], "correta": 0, "disciplina": "Robot Framework"},
    {"pergunta": "Como verificar se um campo está vazio?", "alternativas": ["Textfield Value Should Be", "Field Should Be Empty", "Input Should Be Empty", "Value Should Be Empty"], "correta": 1, "disciplina": "Robot Framework"},
    {"pergunta": "Como executar uma Keyword para cada item de uma lista?", "alternativas": ["FOR", "FOR EACH", "LOOP", "ITERATE"], "correta": 0, "disciplina": "Robot Framework"},

    # Testes de API
    {"pergunta": "O que significa API?", "alternativas": ["Application Programming Interface", "Advanced Programming Integration", "Automated Process Interface", "Application Process Integration"], "correta": 0, "disciplina": "API"},
    {"pergunta": "Qual protocolo é mais comum em APIs web?", "alternativas": ["FTP", "SMTP", "HTTP", "SSH"], "correta": 2, "disciplina": "API"},
    {"pergunta": "O que é um endpoint?", "alternativas": ["Um tipo de dado", "Um endereço de acesso a um recurso da API", "Uma biblioteca de testes", "Um método de autenticação"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que significa REST?", "alternativas": ["Representational State Transfer", "Remote Execution Standard Transfer", "Rapid Endpoint Secure Transfer", "Resource Endpoint Secure Transfer"], "correta": 0, "disciplina": "API"},
    {"pergunta": "Qual método HTTP é usado para criar um recurso?", "alternativas": ["GET", "POST", "PUT", "DELETE"], "correta": 1, "disciplina": "API"},
    {"pergunta": "Qual método HTTP é usado para atualizar um recurso existente?", "alternativas": ["GET", "POST", "PUT", "OPTIONS"], "correta": 2, "disciplina": "API"},
    {"pergunta": "Qual método HTTP remove um recurso?", "alternativas": ["DELETE", "PATCH", "HEAD", "TRACE"], "correta": 0, "disciplina": "API"},
    {"pergunta": "O que significa o status HTTP 200?", "alternativas": ["Recurso criado", "Requisição bem-sucedida", "Recurso não encontrado", "Erro interno do servidor"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que significa o status HTTP 404?", "alternativas": ["Recurso criado", "Recurso não encontrado", "Requisição inválida", "Sem conteúdo"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que significa o status HTTP 500?", "alternativas": ["Erro do cliente", "Recurso não encontrado", "Erro interno do servidor", "Requisição bem-sucedida"], "correta": 2, "disciplina": "API"},
    {"pergunta": "O que é um payload em uma requisição API?", "alternativas": ["O endereço do endpoint", "Os dados enviados na requisição", "O status de resposta", "O método HTTP"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é um header em uma requisição HTTP?", "alternativas": ["O corpo da resposta", "Informações adicionais enviadas na requisição", "O status code", "O endpoint"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é autenticação Basic Auth?", "alternativas": ["Autenticação por token JWT", "Autenticação usando usuário e senha codificados em base64", "Autenticação OAuth2", "Autenticação por IP"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é um token JWT?", "alternativas": ["Um tipo de endpoint", "Um formato de autenticação baseado em JSON", "Um método HTTP", "Um status code"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é o Swagger?", "alternativas": ["Uma ferramenta de versionamento", "Uma ferramenta para documentação e teste de APIs", "Um protocolo de autenticação", "Um tipo de payload"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é Postman?", "alternativas": ["Um framework de automação", "Uma ferramenta para testar APIs", "Um protocolo de rede", "Um tipo de endpoint"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é um teste de contrato em API?", "alternativas": ["Testa a performance da API", "Testa se a API está de acordo com a especificação", "Testa a segurança da API", "Testa a interface gráfica"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é um mock em testes de API?", "alternativas": ["Um endpoint real", "Uma simulação de resposta da API", "Um tipo de autenticação", "Um status code"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é o status HTTP 201?", "alternativas": ["Recurso criado com sucesso", "Recurso não encontrado", "Requisição inválida", "Sem conteúdo"], "correta": 0, "disciplina": "API"},
    {"pergunta": "O que é o status HTTP 204?", "alternativas": ["Requisição bem-sucedida sem conteúdo de resposta", "Recurso criado", "Recurso não encontrado", "Erro de autenticação"], "correta": 0, "disciplina": "API"},
    {"pergunta": "O que é o status HTTP 401?", "alternativas": ["Requisição bem-sucedida", "Não autorizado", "Recurso não encontrado", "Erro interno"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é o status HTTP 403?", "alternativas": ["Proibido/acesso negado", "Recurso criado", "Requisição inválida", "Sem conteúdo"], "correta": 0, "disciplina": "API"},
    {"pergunta": "O que é um teste de carga em API?", "alternativas": ["Testa a documentação", "Testa o comportamento sob alto volume de requisições", "Testa autenticação", "Testa endpoints inválidos"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é um teste negativo em API?", "alternativas": ["Testa apenas casos de sucesso", "Testa respostas para entradas inválidas ou inesperadas", "Testa performance", "Testa autenticação"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é um teste de integração em API?", "alternativas": ["Testa apenas a interface", "Testa a comunicação entre diferentes sistemas via API", "Testa apenas performance", "Testa autenticação"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é um schema em API?", "alternativas": ["Um tipo de autenticação", "Uma definição da estrutura dos dados esperados", "Um status code", "Um endpoint"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é o método PATCH?", "alternativas": ["Atualiza parcialmente um recurso", "Remove um recurso", "Cria um recurso", "Busca um recurso"], "correta": 0, "disciplina": "API"},
    {"pergunta": "O que é o método OPTIONS?", "alternativas": ["Retorna os métodos suportados por um endpoint", "Cria um recurso", "Atualiza um recurso", "Remove um recurso"], "correta": 0, "disciplina": "API"},
    {"pergunta": "O que é um teste de segurança em API?", "alternativas": ["Testa apenas performance", "Testa vulnerabilidades como injeção e autenticação", "Testa documentação", "Testa endpoints inválidos"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é versionamento de API?", "alternativas": ["Atualizar endpoints sem controle", "Manter diferentes versões da API para compatibilidade", "Testar performance", "Testar autenticação"], "correta": 1, "disciplina": "API"},
    {"pergunta": "O que é um rate limit em API?", "alternativas": ["Limite de tamanho do payload", "Limite de requisições permitidas em um período de tempo", "Limite de endpoints", "Limite de autenticação"], "correta": 1, "disciplina": "API"},
 
    # Cypress / Frontend (50 perguntas, nível médio a profissional)
    {"pergunta": "O que é o Cypress?", "alternativas": ["Um framework de backend", "Uma ferramenta de automação de testes end-to-end para aplicações web", "Um gerenciador de pacotes", "Um framework de design"], "correta": 1, "disciplina": "Cypress"},
    {"pergunta": "Como iniciar um projeto Cypress?", "alternativas": ["npm install cypress", "cypress init", "yarn start cypress", "npx cypress create"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Onde ficam os arquivos de teste no Cypress por padrão?", "alternativas": ["src/tests", "cypress/integration", "tests/", "cypress/tests"], "correta": 1, "disciplina": "Cypress"},
    {"pergunta": "Como rodar os testes Cypress em modo interativo?", "alternativas": ["npx cypress open", "cypress run", "npm test", "cypress start"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como rodar os testes Cypress em modo headless?", "alternativas": ["npx cypress run", "cypress headless", "cypress test", "npm run cypress"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Qual comando seleciona um elemento pelo seletor CSS no Cypress?", "alternativas": ["cy.get()", "cy.find()", "cy.select()", "cy.query()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como simular um clique em um botão no Cypress?", "alternativas": ["cy.click()", "cy.get().click()", "cy.press()", "cy.tap()"], "correta": 1, "disciplina": "Cypress"},
    {"pergunta": "Como digitar texto em um campo de input no Cypress?", "alternativas": ["cy.input()", "cy.get().type()", "cy.write()", "cy.sendKeys()"], "correta": 1, "disciplina": "Cypress"},
    {"pergunta": "Como verificar se um texto está visível na página?", "alternativas": ["cy.contains()", "cy.see()", "cy.hasText()", "cy.text()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como fazer uma asserção de que um elemento está visível?", "alternativas": ["cy.get().should('be.visible')", "cy.get().isVisible()", "cy.get().visible()", "cy.get().assertVisible()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como interceptar uma requisição de API no Cypress?", "alternativas": ["cy.intercept()", "cy.route()", "cy.api()", "cy.mock()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como aguardar uma requisição terminar antes de prosseguir?", "alternativas": ["cy.wait()", "cy.pause()", "cy.await()", "cy.sleep()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como fazer upload de arquivo no Cypress?", "alternativas": ["cy.upload()", "cy.get().attachFile()", "cy.fileUpload()", "cy.get().uploadFile()"], "correta": 1, "disciplina": "Cypress"},
    {"pergunta": "Como executar um comando customizado no Cypress?", "alternativas": ["cy.custom()", "cy.exec()", "cy.command()", "cy.run()"], "correta": 1, "disciplina": "Cypress"},
    {"pergunta": "Como acessar variáveis de ambiente no Cypress?", "alternativas": ["Cypress.env()", "cy.env()", "process.env", "cy.getEnv()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como rodar apenas um teste específico?", "alternativas": ["it.only()", "cy.only()", "describe.only()", "test.only()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como rodar apenas um bloco de testes específico?", "alternativas": ["describe.only()", "it.only()", "cy.only()", "test.only()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como pular um teste no Cypress?", "alternativas": ["it.skip()", "cy.skip()", "describe.skip()", "test.skip()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como executar código antes de cada teste?", "alternativas": ["beforeEach()", "before()", "setup()", "init()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como executar código após todos os testes?", "alternativas": ["after()", "afterEach()", "teardown()", "end()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como tirar um screenshot no Cypress?", "alternativas": ["cy.screenshot()", "cy.takeScreenshot()", "cy.capture()", "cy.photo()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como gravar um vídeo da execução dos testes?", "alternativas": ["Cypress grava automaticamente em modo headless", "cy.record()", "cy.video()", "cy.startRecording()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como simular o hover do mouse em um elemento?", "alternativas": ["cy.get().trigger('mouseover')", "cy.get().hover()", "cy.get().mouseOver()", "cy.get().simulateHover()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como selecionar um valor em um dropdown?", "alternativas": ["cy.get().select()", "cy.get().choose()", "cy.get().pick()", "cy.get().dropdown()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como marcar um checkbox?", "alternativas": ["cy.get().check()", "cy.get().mark()", "cy.get().select()", "cy.get().tick()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como desmarcar um checkbox?", "alternativas": ["cy.get().uncheck()", "cy.get().unmark()", "cy.get().deselect()", "cy.get().untick()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como rodar testes em múltiplos navegadores?", "alternativas": ["Usando o argumento --browser", "cy.multiBrowser()", "cy.setBrowser()", "Não é possível"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como simular diferentes tamanhos de tela?", "alternativas": ["cy.viewport()", "cy.resize()", "cy.setScreen()", "cy.screenSize()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como limpar cookies antes de cada teste?", "alternativas": ["cy.clearCookies()", "cy.deleteCookies()", "cy.removeCookies()", "cy.cleanCookies()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como limpar o localStorage?", "alternativas": ["cy.clearLocalStorage()", "cy.deleteLocalStorage()", "cy.removeLocalStorage()", "cy.cleanLocalStorage()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como acessar o valor de um atributo de elemento?", "alternativas": ["cy.get().invoke('attr', 'atributo')", "cy.get().attribute()", "cy.get().getAttribute()", "cy.get().attr()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como esperar por um elemento aparecer na tela?", "alternativas": ["cy.get()", "cy.waitFor()", "cy.await()", "cy.find()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como simular o pressionamento de uma tecla?", "alternativas": ["cy.get().type('{enter}')", "cy.get().press('enter')", "cy.get().sendKeys('enter')", "cy.get().key('enter')"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como acessar o body do documento?", "alternativas": ["cy.get('body')", "cy.body()", "cy.document().body", "cy.root()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como acessar elementos dentro de um iframe?", "alternativas": ["cy.frameLoaded() + cy.iframe()", "cy.get('iframe')", "cy.switchToFrame()", "cy.enterFrame()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como rodar testes em paralelo no CI?", "alternativas": ["Usando Cypress Dashboard e --parallel", "cy.parallel()", "cy.runParallel()", "Não é possível"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como customizar comandos no Cypress?", "alternativas": ["Cypress.Commands.add()", "cy.addCommand()", "cy.customCommand()", "Cypress.addCommand()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como acessar o console do navegador durante o teste?", "alternativas": ["cy.window().then(win => win.console)", "cy.console()", "cy.getConsole()", "cy.log()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como fazer mock de uma resposta de API?", "alternativas": ["cy.intercept()", "cy.mock()", "cy.route()", "cy.apiMock()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como verificar se um elemento possui uma classe CSS?", "alternativas": ["cy.get().should('have.class', 'classe')", "cy.get().hasClass()", "cy.get().class()", "cy.get().assertClass()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como executar comandos JavaScript diretamente na página?", "alternativas": ["cy.window().then(win => {/*...*/})", "cy.execScript()", "cy.runJS()", "cy.js()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como acessar o valor de um input?", "alternativas": ["cy.get().invoke('val')", "cy.get().value()", "cy.get().val()", "cy.get().getValue()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como fazer upload de múltiplos arquivos?", "alternativas": ["cy.get().attachFile(['file1.png', 'file2.png'])", "cy.get().uploadFiles()", "cy.get().multiUpload()", "cy.get().attachFiles()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como rodar testes com diferentes ambientes (dev, qa, prod)?", "alternativas": ["Usando variáveis de ambiente e arquivos de configuração", "cy.setEnv()", "cy.environment()", "cy.envConfig()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como acessar o response de uma requisição interceptada?", "alternativas": ["cy.wait('@alias').then((interception) => { /*...*/ })", "cy.getResponse()", "cy.intercept().response()", "cy.apiResponse()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como rodar testes em diferentes resoluções de tela?", "alternativas": ["cy.viewport()", "cy.screen()", "cy.setResolution()", "cy.setScreenSize()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como simular o scroll da página?", "alternativas": ["cy.scrollTo()", "cy.pageScroll()", "cy.scroll()", "cy.moveScroll()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como verificar se um elemento está desabilitado?", "alternativas": ["cy.get().should('be.disabled')", "cy.get().isDisabled()", "cy.get().disabled()", "cy.get().assertDisabled()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como executar testes de acessibilidade com Cypress?", "alternativas": ["Usando o plugin cypress-axe", "cy.accessibility()", "cy.a11y()", "cy.checkAccessibility()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como rodar testes Cypress em integração contínua (CI)?", "alternativas": ["Usando npx cypress run no pipeline", "cy.ci()", "cy.runCI()", "cy.startCI()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como fazer login programaticamente antes dos testes?", "alternativas": ["cy.request() para autenticação", "cy.login()", "cy.auth()", "cy.programmaticLogin()"], "correta": 0, "disciplina": "Cypress"},
    {"pergunta": "Como ignorar erros não tratados no frontend durante o teste?", "alternativas": ["Cypress.on('uncaught:exception', ...)", "cy.ignoreErrors()", "cy.suppressErrors()", "cy.catchErrors()"], "correta": 0, "disciplina": "Cypress"},

    # Python Básico ao Profissional
    {"pergunta": "O que é uma variável em Python?", "alternativas": ["Um tipo de dado", "Um espaço na memória para armazenar valores", "Uma função", "Um operador lógico"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Como declarar uma função em Python?", "alternativas": ["function minha_funcao():", "def minha_funcao():", "fun minha_funcao():", "declare minha_funcao():"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Qual comando imprime algo na tela?", "alternativas": ["echo()", "print()", "show()", "display()"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Como comentar uma linha em Python?", "alternativas": ["// comentário", "# comentário", "<!-- comentário -->", "-- comentário"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Qual o resultado de 2 + 3 * 4 em Python?", "alternativas": ["20", "14", "24", "9"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Como criar uma lista em Python?", "alternativas": ["lista = {}", "lista = []", "lista = ()", "lista = <>"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Como acessar o primeiro elemento de uma lista chamada 'itens'?", "alternativas": ["itens[0]", "itens(1)", "itens{0}", "itens[1]"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como adicionar um item ao final de uma lista?", "alternativas": ["lista.add()", "lista.append()", "lista.push()", "lista.insert()"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Qual a função para obter o tamanho de uma lista?", "alternativas": ["size(lista)", "count(lista)", "len(lista)", "length(lista)"], "correta": 2, "disciplina": "Python"},
    {"pergunta": "Como criar um dicionário em Python?", "alternativas": ["d = []", "d = {}", "d = ()", "d = <>"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Como acessar o valor da chave 'nome' em um dicionário d?", "alternativas": ["d['nome']", "d.nome", "d[nome]", "d->nome"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Qual a saída de print(type(10))?", "alternativas": ["<class 'int'>", "<type 'int'>", "int", "integer"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como converter uma string '123' para inteiro?", "alternativas": ["int('123')", "str(123)", "float('123')", "toInt('123')"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Qual operador é usado para igualdade?", "alternativas": ["=", "==", "===", "!="], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Como criar um loop de 0 a 4?", "alternativas": ["for i in range(5):", "for i = 0 to 4:", "for i in 0..4:", "for (i=0; i<5; i++):"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como verificar se x está em lista?", "alternativas": ["x in lista", "lista.has(x)", "x dentro lista", "lista.contains(x)"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como tratar exceções em Python?", "alternativas": ["try/catch", "try/except", "try/handle", "try/onerror"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Qual comando encerra um loop?", "alternativas": ["stop", "break", "exit", "end"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Como importar o módulo math?", "alternativas": ["import math", "include math", "using math", "require math"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como ler uma linha do teclado?", "alternativas": ["input()", "read()", "scan()", "get()"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Qual a saída de print('a' * 3)?", "alternativas": ["aaa", "a3", "a a a", "Erro"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como remover espaços em branco de uma string s?", "alternativas": ["s.trim()", "s.strip()", "s.clean()", "s.removeSpaces()"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Como inverter uma lista l?", "alternativas": ["l.reverse()", "reverse(l)", "l.invert()", "l[::-1]"], "correta": 3, "disciplina": "Python"},
    {"pergunta": "Como criar um conjunto (set)?", "alternativas": ["seta = []", "seta = set()", "seta = {}", "seta = ()"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Como abrir um arquivo para leitura?", "alternativas": ["open('arq.txt', 'r')", "file('arq.txt')", "open('arq.txt', 'w')", "read('arq.txt')"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como verificar o tipo de uma variável x?", "alternativas": ["typeof(x)", "type(x)", "x.type()", "gettype(x)"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Qual a saída de print(10//3)?", "alternativas": ["3.33", "3", "3.0", "4"], "correta": 1, "disciplina": "Python"},
    {"pergunta": "Como criar uma função lambda que soma dois números?", "alternativas": ["lambda x, y: x + y", "def soma(x, y): x + y", "lambda(x, y) x + y", "sum = lambda x, y: x + y"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como ordenar uma lista l crescente?", "alternativas": ["l.sort()", "sort(l)", "l.order()", "l.sorted()"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como criar uma classe em Python?", "alternativas": ["class MinhaClasse:", "classe MinhaClasse:", "def MinhaClasse:", "object MinhaClasse:"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como definir um construtor em uma classe?", "alternativas": ["def __init__(self):", "def init(self):", "def construtor(self):", "def __start__(self):"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como herdar de uma classe Base?", "alternativas": ["class Derivada(Base):", "class Derivada extends Base:", "class Derivada[Base]:", "class Derivada.Base:"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como criar um módulo em Python?", "alternativas": ["Arquivo .py", "Arquivo .mod", "Arquivo .module", "Arquivo .pyc"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como instalar um pacote com pip?", "alternativas": ["pip install pacote", "pip add pacote", "pip get pacote", "pip download pacote"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como criar um ambiente virtual?", "alternativas": ["python -m venv venv", "virtualenv venv", "pip venv", "pyenv venv"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como verificar a versão do Python?", "alternativas": ["python --version", "python -v", "py --ver", "python version"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como fazer f-strings?", "alternativas": ["f\"texto {variavel}\"", "\"texto {variavel}\"", "format('texto', variavel)", "f'texto' + variavel"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como criar um generator?", "alternativas": ["Usando yield", "Usando return", "Usando generate", "Usando gen()"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como manipular datas em Python?", "alternativas": ["datetime", "dateutil", "calendar", "date"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como fazer importação relativa?", "alternativas": ["from .modulo import x", "import ./modulo", "from modulo import x", "relative import modulo"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como criar um decorador?", "alternativas": ["@decorador", "#decorador", "decorador()", "decorator:"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como serializar para JSON?", "alternativas": ["json.dumps()", "json.save()", "json.write()", "json.serialize()"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como ler JSON de um arquivo?", "alternativas": ["json.load()", "json.loads()", "json.read()", "json.parse()"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como criar um arquivo temporário?", "alternativas": ["tempfile.TemporaryFile()", "os.tempfile()", "file.temp()", "tempfile.create()"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como capturar argumentos de linha de comando?", "alternativas": ["sys.argv", "os.args", "argparse.args", "input.args"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como fazer testes unitários?", "alternativas": ["unittest", "pytest", "nose", "Todas as anteriores"], "correta": 3, "disciplina": "Python"},
    {"pergunta": "Como criar uma exceção customizada?", "alternativas": ["class MinhaExcecao(Exception):", "def MinhaExcecao(Exception):", "MinhaExcecao = Exception()", "raise MinhaExcecao"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como usar list comprehension?", "alternativas": ["[x for x in lista]", "for x in lista: x", "list(x for x in lista)", "[x in lista]"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como abrir um arquivo com encoding utf-8?", "alternativas": ["open('arq.txt', encoding='utf-8')", "open('arq.txt', 'utf-8')", "file('arq.txt', 'utf-8')", "open('arq.txt', code='utf-8')"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como usar o with para arquivos?", "alternativas": ["with open('arq.txt') as f:", "open('arq.txt') as f:", "with file('arq.txt') as f:", "with open('arq.txt', 'with') as f:"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como criar um property em uma classe?", "alternativas": ["@property", "@get", "@prop", "@attribute"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como fazer logging?", "alternativas": ["import logging", "import log", "import logger", "import logs"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como obter o diretório atual?", "alternativas": ["os.getcwd()", "os.pwd()", "os.curdir()", "os.dir()"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como executar um comando do sistema?", "alternativas": ["os.system()", "sys.exec()", "os.exec()", "system.run()"], "correta": 0, "disciplina": "Python"},
    {"pergunta": "Como criar um pacote Python?", "alternativas": ["Pasta com __init__.py", "Arquivo .py", "Arquivo .zip", "Arquivo .egg"], "correta": 0, "disciplina": "Python"},

    # DevOps Cultura Agil
    {"pergunta": "O que é DevOps?", "alternativas": ["Uma linguagem de programação", "Uma metodologia que integra desenvolvimento e operações", "Um sistema operacional", "Um framework de testes"], "correta": 1, "disciplina": "DevOps"},
    {"pergunta": "Qual o principal objetivo do DevOps?", "alternativas": ["Aumentar a burocracia", "Reduzir o tempo de entrega e aumentar a qualidade", "Separar times de dev e ops", "Automatizar apenas testes"], "correta": 1, "disciplina": "DevOps"},
    {"pergunta": "O que significa CI em DevOps?", "alternativas": ["Continuous Integration", "Code Inspection", "Cloud Infrastructure", "Continuous Improvement"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que significa CD em DevOps?", "alternativas": ["Continuous Delivery/Deployment", "Code Development", "Cloud Deployment", "Continuous Debug"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "Qual ferramenta é usada para integração contínua?", "alternativas": ["Jenkins", "Photoshop", "Excel", "Word"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é pipeline de CI/CD?", "alternativas": ["Uma linha de montagem de software", "Um processo automatizado de build, teste e deploy", "Um tipo de banco de dados", "Uma linguagem de script"], "correta": 1, "disciplina": "DevOps"},
    {"pergunta": "O que é infraestrutura como código (IaC)?", "alternativas": ["Infraestrutura manual", "Infraestrutura definida e gerenciada por código", "Infraestrutura terceirizada", "Infraestrutura física"], "correta": 1, "disciplina": "DevOps"},
    {"pergunta": "Qual ferramenta é usada para IaC?", "alternativas": ["Terraform", "Excel", "Notepad", "Paint"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é um container?", "alternativas": ["Um tipo de servidor físico", "Uma unidade leve de software que empacota código e dependências", "Um arquivo zip", "Um banco de dados"], "correta": 1, "disciplina": "DevOps"},
    {"pergunta": "Qual ferramenta é mais usada para containers?", "alternativas": ["Docker", "Photoshop", "Excel", "Git"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é orquestração de containers?", "alternativas": ["Gerenciar múltiplos containers automaticamente", "Tocar música com containers", "Compactar containers", "Desenhar containers"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "Qual ferramenta é referência em orquestração de containers?", "alternativas": ["Kubernetes", "Jenkins", "Terraform", "Excel"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é monitoramento em DevOps?", "alternativas": ["Acompanhar métricas e logs de sistemas", "Apenas olhar o sistema", "Fazer backup", "Desenvolver código"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "Qual ferramenta é usada para monitoramento?", "alternativas": ["Prometheus", "Word", "Excel", "Paint"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é cultura ágil?", "alternativas": ["Foco em processos rígidos", "Foco em colaboração, adaptação e entregas frequentes", "Foco em documentação", "Foco em hierarquia"], "correta": 1, "disciplina": "DevOps"},
    {"pergunta": "O que é Scrum?", "alternativas": ["Um framework ágil para gestão de projetos", "Uma linguagem de programação", "Um banco de dados", "Um sistema operacional"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é Kanban?", "alternativas": ["Um método visual de gestão de fluxo de trabalho", "Uma linguagem de script", "Um tipo de servidor", "Um framework de testes"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é backlog no Scrum?", "alternativas": ["Lista priorizada de tarefas a serem feitas", "Um bug", "Um tipo de deploy", "Um relatório"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é sprint?", "alternativas": ["Período de tempo para entregar um conjunto de tarefas", "Uma reunião", "Um bug", "Um deploy"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é daily?", "alternativas": ["Reunião diária de alinhamento do time", "Deploy diário", "Backup diário", "Bug diário"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é retrospectiva?", "alternativas": ["Reunião para analisar o que funcionou e o que pode melhorar", "Deploy", "Bug", "Backup"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é automação de testes?", "alternativas": ["Execução automática de testes de software", "Testes manuais", "Deploy manual", "Backup automático"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é rollback?", "alternativas": ["Reverter uma mudança/deploy para o estado anterior", "Deploy", "Backup", "Bug"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é blue-green deployment?", "alternativas": ["Estratégia de deploy com dois ambientes para minimizar downtime", "Deploy manual", "Deploy noturno", "Deploy em produção"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é feature toggle?", "alternativas": ["Habilitar/desabilitar funcionalidades sem novo deploy", "Deploy manual", "Backup", "Bug"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é lead time?", "alternativas": ["Tempo entre início e entrega de uma demanda", "Tempo de deploy", "Tempo de backup", "Tempo de bug"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é MTTR?", "alternativas": ["Mean Time To Recovery", "Mean Time To Run", "Mean Time To Release", "Mean Time To Retry"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é trunk based development?", "alternativas": ["Desenvolvimento focado em uma única branch principal", "Desenvolvimento em múltiplas branches longas", "Deploy manual", "Backup"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é observabilidade?", "alternativas": ["Capacidade de entender o que está acontecendo no sistema através de logs, métricas e traces", "Backup", "Deploy", "Bug"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é feedback rápido?", "alternativas": ["Receber retorno sobre mudanças rapidamente", "Deploy manual", "Backup", "Bug"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é um artefato em DevOps?", "alternativas": ["Arquivo gerado pelo processo de build (ex: .jar, .zip)", "Bug", "Deploy", "Backup"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é versionamento de configuração?", "alternativas": ["Controlar versões de arquivos de configuração como código", "Backup", "Deploy", "Bug"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é um playbook no Ansible?", "alternativas": ["Arquivo YAML que define automações de infraestrutura", "Bug", "Deploy", "Backup"], "correta": 0, "disciplina": "DevOps"},
    {"pergunta": "O que é cultura de colaboração?", "alternativas": ["Trabalho conjunto entre dev, ops e outras áreas", "Trabalho isolado", "Backup", "Deploy"], "correta": 0, "disciplina": "DevOps"},

    # BDD e Gherkin
    {"pergunta": "O que significa BDD?", "alternativas": ["Behavior-Driven Development", "Bug-Driven Development", "Business Data Design", "Base Data Development"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é Gherkin?", "alternativas": ["Linguagem para escrever cenários de teste BDD", "Framework de automação", "Ferramenta de CI/CD", "Biblioteca de logs"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Qual palavra-chave inicia um cenário em Gherkin?", "alternativas": ["Scenario", "Given", "Feature", "Background"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Qual palavra-chave define o contexto inicial em Gherkin?", "alternativas": ["Given", "When", "Then", "And"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Qual palavra-chave indica uma ação em Gherkin?", "alternativas": ["When", "Given", "Then", "But"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Qual palavra-chave indica o resultado esperado em Gherkin?", "alternativas": ["Then", "Given", "When", "And"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como reutilizar passos em Gherkin?", "alternativas": ["And/But", "Repeat", "Reuse", "Loop"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é uma Feature em Gherkin?", "alternativas": ["Descrição de uma funcionalidade", "Descrição de um bug", "Descrição de um teste unitário", "Descrição de um deploy"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é um Step Definition?", "alternativas": ["Código que implementa os passos do Gherkin", "Arquivo de configuração", "Script de deploy", "Relatório de testes"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Qual extensão de arquivo para cenários Gherkin?", "alternativas": [".feature", ".gherkin", ".bdd", ".test"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é Background em Gherkin?", "alternativas": ["Contexto comum a todos os cenários", "Cenário de erro", "Cenário de sucesso", "Cenário ignorado"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como parametrizar cenários em Gherkin?", "alternativas": ["Scenario Outline", "Scenario Param", "Scenario Loop", "Scenario Data"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Qual palavra-chave define exemplos em Scenario Outline?", "alternativas": ["Examples", "Sample", "Data", "Cases"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é Cucumber?", "alternativas": ["Ferramenta para executar testes BDD", "Framework de frontend", "Ferramenta de deploy", "Biblioteca de logs"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como comentários são feitos em Gherkin?", "alternativas": ["# comentário", "// comentário", "-- comentário", "/* comentário */"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é Step Reuse em BDD?", "alternativas": ["Reutilizar passos em diferentes cenários", "Repetir cenários", "Repetir features", "Reutilizar arquivos"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como ignorar um cenário em Gherkin?", "alternativas": ["Tag @ignore", "Tag @skip", "Tag @disabled", "Tag @omit"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é uma tag em Gherkin?", "alternativas": ["Marcador para agrupar ou filtrar cenários", "Palavra-chave obrigatória", "Comentário", "Nome do arquivo"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como executar apenas cenários com uma tag específica?", "alternativas": ["Usando --tags na linha de comando", "Usando --filter", "Usando --only", "Usando --scenario"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é Given-When-Then?", "alternativas": ["Estrutura básica de um cenário BDD", "Estrutura de um teste unitário", "Estrutura de um deploy", "Estrutura de um commit"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é um cenário negativo em BDD?", "alternativas": ["Testa comportamentos inesperados ou inválidos", "Testa apenas sucesso", "Testa performance", "Testa integração"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como documentar regras de negócio em BDD?", "alternativas": ["Usando Features e cenários", "Usando README", "Usando scripts SQL", "Usando diagramas"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é automação de BDD?", "alternativas": ["Executar cenários Gherkin via código", "Executar scripts SQL", "Executar deploy", "Executar backups"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como validar múltiplos resultados em Then?", "alternativas": ["Usando múltiplos Then ou And", "Usando Repeat", "Usando Loop", "Usando Validate"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é um cenário Outline?", "alternativas": ["Cenário com parâmetros e exemplos", "Cenário ignorado", "Cenário de erro", "Cenário de sucesso"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como passar dados para Steps em Gherkin?", "alternativas": ["Usando parâmetros entre < >", "Usando variáveis de ambiente", "Usando arquivos .env", "Usando funções"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é um exemplo em Scenario Outline?", "alternativas": ["Linha de dados para executar o cenário", "Comentário", "Tag", "Feature"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como organizar arquivos .feature?", "alternativas": ["Por funcionalidade", "Por usuário", "Por data", "Por tamanho"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é um passo pendente em BDD?", "alternativas": ["Step sem implementação de código", "Step ignorado", "Step duplicado", "Step inválido"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como tratar Steps duplicados?", "alternativas": ["Reutilizar Step Definitions", "Excluir Steps", "Ignorar Steps", "Renomear Steps"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é integração contínua com BDD?", "alternativas": ["Executar cenários BDD em pipelines CI", "Executar scripts SQL", "Executar deploy manual", "Executar backups"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como gerar relatórios de execução BDD?", "alternativas": ["Ferramentas como Cucumber Reports", "Excel", "Word", "Paint"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é Living Documentation?", "alternativas": ["Documentação gerada automaticamente a partir dos cenários BDD", "Documentação em PDF", "Documentação manual", "Documentação em vídeo"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como garantir que Steps sejam claros e objetivos?", "alternativas": ["Usar linguagem natural e simples", "Usar termos técnicos", "Usar abreviações", "Usar código"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é um anti-pattern em BDD?", "alternativas": ["Prática que dificulta manutenção dos cenários", "Prática recomendada", "Prática obrigatória", "Prática de deploy"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como evitar Steps genéricos demais?", "alternativas": ["Ser específico no comportamento esperado", "Usar apenas And", "Usar apenas Given", "Usar apenas Then"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é um cenário de aceitação?", "alternativas": ["Cenário que valida requisitos do usuário", "Cenário de erro", "Cenário de performance", "Cenário de deploy"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como relacionar cenários BDD com User Stories?", "alternativas": ["Cada User Story pode ter vários cenários BDD", "Cada User Story tem um cenário", "Cada User Story tem um Step", "Cada User Story tem uma Feature"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "O que é um cenário feliz (happy path)?", "alternativas": ["Fluxo principal de sucesso", "Fluxo de erro", "Fluxo alternativo", "Fluxo de rollback"], "correta": 0, "disciplina": "BDD"},
    {"pergunta": "Como tratar cenários alternativos em BDD?", "alternativas": ["Criando cenários separados para cada variação", "Ignorando", "Comentando", "Usando apenas um cenário"], "correta": 0, "disciplina": "BDD"},

    # Vocabulário de TI
    {"pergunta": "O que significa 'deploy' em TI?", "alternativas": ["Desenvolver código", "Publicar uma aplicação em produção", "Testar um sistema", "Remover um sistema"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'backend'?", "alternativas": ["Parte visual do sistema", "Parte lógica e de processamento do sistema", "Banco de dados", "Interface do usuário"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'frontend'?", "alternativas": ["Banco de dados", "Parte lógica do sistema", "Interface visual com o usuário", "Servidor"], "correta": 2, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que significa 'bug'?", "alternativas": ["Funcionalidade nova", "Erro ou falha no sistema", "Atualização de software", "Backup"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'commit'?", "alternativas": ["Salvar alterações no repositório de código", "Remover código", "Executar testes", "Atualizar o sistema"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'merge'?", "alternativas": ["Dividir código", "Unir alterações de diferentes branches", "Remover branch", "Criar backup"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'pull request'?", "alternativas": ["Solicitação para unir código de uma branch em outra", "Remover código", "Executar testes", "Atualizar dependências"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que significa 'rollback'?", "alternativas": ["Avançar para nova versão", "Reverter para versão anterior", "Atualizar sistema", "Executar testes"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'endpoint'?", "alternativas": ["Banco de dados", "URL de acesso a um recurso de API", "Interface gráfica", "Servidor"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'framework'?", "alternativas": ["Linguagem de programação", "Conjunto de ferramentas e bibliotecas para desenvolvimento", "Banco de dados", "Sistema operacional"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'API'?", "alternativas": ["Interface de Programação de Aplicações", "Banco de dados", "Sistema operacional", "Framework"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que significa 'refatorar'?", "alternativas": ["Adicionar funcionalidades", "Melhorar o código sem alterar comportamento", "Remover código", "Executar testes"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'hotfix'?", "alternativas": ["Nova funcionalidade", "Correção rápida de bug em produção", "Atualização de dependências", "Backup"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'release'?", "alternativas": ["Remover código", "Publicação de uma nova versão do sistema", "Executar testes", "Atualizar dependências"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'patch'?", "alternativas": ["Nova funcionalidade", "Correção ou atualização pequena em software", "Remover código", "Executar testes"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'build'?", "alternativas": ["Processo de compilar e empacotar o sistema", "Executar testes", "Remover código", "Atualizar dependências"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'branch'?", "alternativas": ["Banco de dados", "Linha de desenvolvimento paralela no controle de versão", "Servidor", "Framework"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'token'?", "alternativas": ["Senha de banco de dados", "Chave de autenticação ou autorização", "Framework", "Servidor"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'container'?", "alternativas": ["Banco de dados", "Unidade leve de software que empacota código e dependências", "Framework", "Servidor"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'cloud'?", "alternativas": ["Banco de dados", "Serviços de computação em nuvem", "Framework", "Servidor local"], "correta": 1, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'script'?", "alternativas": ["Arquivo de código executável", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'log'?", "alternativas": ["Registro de eventos e informações do sistema", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'debug'?", "alternativas": ["Processo de encontrar e corrigir erros no código", "Atualizar dependências", "Remover código", "Executar testes"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'pipeline'?", "alternativas": ["Processo automatizado de build, teste e deploy", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'proxy'?", "alternativas": ["Servidor intermediário entre cliente e servidor final", "Banco de dados", "Framework", "Script"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'DNS'?", "alternativas": ["Sistema de nomes de domínio", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'firewall'?", "alternativas": ["Sistema de proteção de rede", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'endpoint' em API?", "alternativas": ["URL de acesso a um recurso", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'latência'?", "alternativas": ["Tempo de resposta de uma requisição", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'timeout'?", "alternativas": ["Tempo limite para uma operação", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'cache'?", "alternativas": ["Armazenamento temporário para agilizar acessos", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'payload'?", "alternativas": ["Conteúdo de dados enviado em uma requisição", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'endpoint seguro'?", "alternativas": ["Recurso protegido por autenticação/autorização", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'token JWT'?", "alternativas": ["Token de autenticação baseado em JSON", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'hash'?", "alternativas": ["Função que gera valor único para dados", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'criptografia'?", "alternativas": ["Técnica para proteger dados", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'endpoint público'?", "alternativas": ["Recurso acessível sem autenticação", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'endpoint privado'?", "alternativas": ["Recurso que exige autenticação/autorização", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'deploy automatizado'?", "alternativas": ["Publicação automática do sistema", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'ambiente de homologação'?", "alternativas": ["Ambiente para testes antes da produção", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'ambiente de produção'?", "alternativas": ["Ambiente real utilizado por usuários finais", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'ambiente de desenvolvimento'?", "alternativas": ["Ambiente usado por desenvolvedores para criar/testar código", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'endpoint REST'?", "alternativas": ["Recurso de API seguindo padrão REST", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'endpoint SOAP'?", "alternativas": ["Recurso de API seguindo padrão SOAP", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'webhook'?", "alternativas": ["Notificação automática via HTTP quando evento ocorre", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'endpoint de callback'?", "alternativas": ["URL para receber resposta de processamento assíncrono", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'endpoint de healthcheck'?", "alternativas": ["Recurso para verificar se sistema está funcionando", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'endpoint de status'?", "alternativas": ["Recurso que retorna informações sobre o sistema", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'endpoint versionado'?", "alternativas": ["Recurso de API com controle de versão", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'endpoint de autenticação'?", "alternativas": ["Recurso para login/autorização de usuários", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},
    {"pergunta": "O que é 'endpoint de logout'?", "alternativas": ["Recurso para encerrar sessão do usuário", "Banco de dados", "Framework", "Servidor"], "correta": 0, "disciplina": "Vocabulário TI"},

    # Azure e Dashboard

]

disciplinas = {}
for p in perguntas:
    if p['disciplina'] not in disciplinas:
        disciplinas[p['disciplina']] = {"acertos": 0, "erros": 0}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Processo Seletivo")
        self.index = -1
        self.tempo_restante = 40
        self.timer_after_id = None

        self.resultado_final = disciplinas.copy()

        if os.path.exists(RESULTADO_ARQUIVO):
            self.mostrar_resultado_final()
            return

        self.exibir_regras()

    def exibir_regras(self):
        self.clear()
        tk.Label(self.root, text="LEIA COM ATENÇÃO", font=("Helvetica", 17, "bold")).pack(pady=20)
        regras = (
            "- Você terá 40 segundos para responder cada pergunta.\n"
            "- Caso não responda, contará como erro.\n"
            "- Acertos: +1 ponto / Erros: -1 ponto (por disciplina).\n"
            "- Após finalizar, o resultado será exibido.\n"
            "- O teste só pode ser executado UMA única vez."
        )
        tk.Label(self.root, text=regras, font=("Helvetica", 15), wraplength=840, justify="left").pack(pady=20)
        self.timer_label = tk.Label(self.root, text="Iniciando em 600s", font=("Helvetica", 14), fg="red")
        self.timer_label.pack()
        self.countdown(6, self.iniciar_quiz)

    def iniciar_quiz(self):
        self.index = -1
        self.proxima_pergunta()

    def proxima_pergunta(self):
        self.index += 1
        self.tempo_restante = 40

        if self.index >= len(perguntas):
            self.salvar_resultado()
            self.mostrar_resultado_final()
            return

        self.clear()
        self.pergunta_atual = perguntas[self.index]
        tk.Label(
            self.root,
            text=self.pergunta_atual['pergunta'],
            font=("Helvetica", 14, "bold"),
            wraplength=550,
            justify="center"
        ).pack(pady=20)

        for i, alt in enumerate(self.pergunta_atual['alternativas']):
            tk.Button(self.root, text=alt, font=("Helvetica", 12), width=70, command=lambda i=i: self.responder(i)).pack(pady=5)

        self.timer_label = tk.Label(self.root, text="Tempo restante: 40s", fg="red", font=("Helvetica", 12))
        self.timer_label.pack(pady=10)
        self.countdown(40, self.tempo_expirado)

    def responder(self, resposta):
        self.cancelar_timer()
        correta = self.pergunta_atual['correta']
        disciplina = self.pergunta_atual['disciplina']

        if resposta == correta:
            self.resultado_final[disciplina]['acertos'] += 1
        else:
            self.resultado_final[disciplina]['erros'] += 1

        self.proxima_pergunta()

    def tempo_expirado(self):
        self.cancelar_timer()
        disciplina = self.pergunta_atual['disciplina']
        self.resultado_final[disciplina]['erros'] += 1
        self.proxima_pergunta()

    def countdown(self, segundos, callback):
        def atualizar():
            if segundos <= 0:
                callback()
                return
            self.timer_label.config(text=f"Tempo restante: {segundos}s")
            self.timer_after_id = self.root.after(1000, lambda: self.countdown(segundos - 1, callback))

        self.cancelar_timer()
        atualizar()

    def cancelar_timer(self):
        if self.timer_after_id:
            self.root.after_cancel(self.timer_after_id)
            self.timer_after_id = None

    def salvar_resultado(self):
        with open(RESULTADO_ARQUIVO, 'w') as f:
            json.dump(self.resultado_final, f)

    def mostrar_resultado_final(self):
        self.clear()
        tk.Label(self.root, text="RESULTADO FINAL", font=("Helvetica", 16, "bold"), fg="green").pack(pady=10)

        total_acertos = 0
        total_erros = 0

        for disc, res in self.resultado_final.items():
            acertos = res['acertos']
            erros = res['erros']
            total = acertos + erros
            total_acertos += acertos
            total_erros += erros
            percentual = int((acertos / total) * 100) if total > 0 else 0
            tk.Label(self.root, text=f"{disc}: {acertos} acertos, {erros} erros - {percentual}% de acerto", font=("Helvetica", 12)).pack(pady=3)

        total_respostas = total_acertos + total_erros
        total_percent = int((total_acertos / total_respostas) * 100) if total_respostas > 0 else 0
        tk.Label(self.root, text=f"\nTOTAL: {total_acertos} acertos / {total_erros} erros - {total_percent}% de acerto", font=("Helvetica", 14, "bold"), fg="blue").pack(pady=20)

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("900x600")  # Aumentado para caber perguntas longas com padding
    app = QuizApp(root)
    root.mainloop()
