from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

class Visual (Console):
	def __init__(self)-> None:
		super().__init__()
		
	def message(self, caption: str, content: str, fgStyle: str, bgStyle: str)-> None:
		messageCaption: str=f"[{fgStyle} on {bgStyle}]{caption}[/{fgStyle} on {bgStyle}]"
		messageContent: str=f"[{bgStyle} on {fgStyle}]{content}[/{bgStyle} on {fgStyle}]"
		panel: Panel=Panel(messageContent, title=messageCaption, border_style=bgStyle)
		self.print(panel)
	
	def prompt(self, caption: str, fgStyle: str, bgStyle: str)-> str:
		result: str=Prompt.ask(f"[{fgStyle} on {bgStyle}]{caption}[/{fgStyle} on {bgStyle}]")
		return result
		
	def confirm(self, caption: str, fgStyle: str, bgStyle: str)-> bool:
		result: bool=Confirm.ask(f"[{fgStyle} on {bgStyle}]{caption}[/{fgStyle} on {bgStyle}]")
		return result

class App (Visual):
		def __init__(self)-> None:
			super().__init__()
		def config_rtu(self)-> dict[str,str, int, int, int, int]:
			settings: dict[str, str, int, int, int, int]=dict()
			self.message("Настройка подключения", "Введиде необходимые параметры подключения. Их можно пооучить из настроек контроллера", "white", "blue")
			while True:
				settings["port"]=self.prompt("Порт", "blue", "white")
				settings["parity"]=self.prompt("Четность", "blue", "white")
				try:
					settings["baudrate"]=int(self.prompt("Количество бод", "blue", "white"))
					settings["byte_size"]=int(self.prompt("Размер байта", "blue", "white"))
					settings["stop_bits"]=int(self.prompt("Стоп-биты", "blue", "white"))
					settings["timeout"]=int(self.prompt("Таймаут соединения", "blue", "white"))
				except ValueError:
					if self.confirm("Задано не числовое значение! Начать сначала (у) или принять значения по умолчанию (n)?", "white", "red"):
						continue
					else:
						settings["port"]="COM3"
						settings["parity"]="none"
						settings["baudrate"]=9600
						settings["byte_size"]=8
						settings["stop_bits"]=2
						settings["timeout"]=5
				if self.confirm("Применить настройки?", "white", "blue"):
						break
				else:
						continue
						
		def main_menu(self)-> str:
			menuCaption: str="Главное меню"
			menuItems: str=" 1. Монитор состояния \n 2. Настройка соединения \n 3. Ручное управление \n 4. Завершить сеанс"
			self.clear()
			self.message(menuCaption, menuItems, "white", "green")
			return self.prompt("Выбранный пункт: ", "green", "white")
						

		