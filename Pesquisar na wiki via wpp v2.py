from selenium import webdriver
import time
import wikipedia


class RobotAssistente:
    def __init__(self, contato):
        self.contato = contato
        try:
            # instância o local do cromedriver
            self.chrome = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
            # Recebe o site que precisa entrar
            self.chrome.get('https://web.whatsapp.com/')
            time.sleep(15)
        except Exception as err:
            print('Erro: chromedriver | acesso ao site\n', err)
        else:
            self.pergunta = self.ver_msg_contato(self.contato)
            self.pesquisar_wiki_enviar(self.pergunta)

    def ver_msg_contato(self, contato):
        try:
            primeira_caixa = self.chrome.find_element_by_xpath(f'//span[@title="{contato}"]')
            primeira_caixa.click()

            post = self.chrome.find_elements_by_class_name("_3_7SH")
            ultimo = len(post) - 1
            # O texto da ultima mensagem
            texto_recebido = post[ultimo].find_element_by_css_selector("span.selectable-text").text

            print(f'Pesquisa do contato {contato}: {texto_recebido}', )

        except Exception as erro:
            print('Erro\n', erro)
        else:
            return texto_recebido

    def pesquisar_wiki_enviar(self, palavra):
        try:
            wikipedia.set_lang('pt')
            mensagem = wikipedia.summary(palavra)
        except Exception as err:
            print('Ocorreu um erro ao realizar essa pesquisa\n', err)
            caixa_texto = self.chrome.find_element_by_class_name('_1Plpp')
            caixa_texto.send_keys('Desculpe, Não consegui encontrar o que deseja tente perguntar de outra forma')
            time.sleep(0.30)
            btn_enviar = self.chrome.find_element_by_xpath('//span[@data-icon="send"]')
            btn_enviar.click()

        else:
            print(mensagem)
            caixa_texto = self.chrome.find_element_by_class_name('_1Plpp')
            caixa_texto.send_keys(mensagem)
            time.sleep(0.30)
            btn_enviar = self.chrome.find_element_by_xpath('//span[@data-icon="send"]')
            btn_enviar.click()


if __name__ == '__main__':
    RobotAssistente('Gaby Lourenço')
