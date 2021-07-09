from selenium import webdriver
import time
import wikipedia


try:
    chrome = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
    chrome.get('https://web.whatsapp.com/')
    # Tempo para colocar o QR
    time.sleep(10)

    def enviar_msg(palavra):
        try:
            wikipedia.set_lang('pt')
            mensagem = wikipedia.summary(palavra)
        except Exception as err:
            print('Ocorreu um erro ao realizar essa pesquisa\n', err)
            caixa_texto = chrome.find_element_by_class_name('_1Plpp')
            caixa_texto.send_keys('Desculpe, Não consegui encontrar o que deseja tente perguntar de outra forma')
            time.sleep(0.30)
            btn_enviar = chrome.find_element_by_xpath('//span[@data-icon="send"]')
            btn_enviar.click()

        else:
            print(mensagem)
            caixa_texto = chrome.find_element_by_class_name('_1Plpp')
            caixa_texto.send_keys(mensagem)
            time.sleep(0.30)
            btn_enviar = chrome.find_element_by_xpath('//span[@data-icon="send"]')
            btn_enviar.click()

except Exception as err:
    print('ERRO: webdriver ou link do site\n', err)
else:
    try:
        primeira_caixa = chrome.find_element_by_xpath('//span[@title="Gaby Lourenço"]')
        primeira_caixa.click()

        post = chrome.find_elements_by_class_name("_3_7SH")
        ultimo = len(post) - 1
        # O texto da ultima mensagem
        texto = post[ultimo].find_element_by_css_selector("span.selectable-text").text
        enviar_msg(texto)
        print(texto)
    except Exception as err:
        print('Erro\n', err)
    else:
        # fecha o chrome
        chrome.quit()



