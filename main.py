from kivy.app import App
from kivy.lang import Builder
import requests 

GUI = Builder.load_file("tela.kv")


class meuAplicativo(App):

  def build(self):
    return GUI

  
  def on_start(self):
    print("Aplicativo iniciado")
    self.root.ids["moeda1"].text = f"Dólar R$ {self.get_cotacao('USD')}"
    self.root.ids["moeda2"].text = f"Euro R$ {self.get_cotacao('EUR')}"
    self.root.ids["moeda3"].text = f"Libra R$ {self.get_cotacao('GBP')}"
    self.root.ids["moeda4"].text = f"Peso Argentino R$ {self.get_cotacao('ARS')}"

  
  def get_cotacao(self, moeda):
    link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()
    cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
    return cotacao
    
    
    

meuAplicativo().run()